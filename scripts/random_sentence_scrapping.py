from requests import get
from scrapy import Selector
import string
import re 

wiki_url = 'https://fr.wikipedia.org/wiki/Sp%C3%A9cial:Page_au_hasard'

def scrap_random_wiki_page():
	response = get(wiki_url)
	source = None
	if response.status_code == 200 :
	    source = response.text
	if source :
		selector = Selector(text=source)
		content = selector.css("#bodyContent p")
		#print(content.extract())
		text_content = content.xpath('.//text()').extract()
		full_text=''.join(text_content)
		sentence_array = full_text.split('.')
		clean_sentence_array = []
		for sentence in sentence_array:
			lower_sentence = sentence.lower()
			if not(lower_sentence.__contains__('wiki')):
				clean_sentence = re.sub("([\[]).*?([\]])", "", sentence)
				clean_sentence = clean_sentence.translate(str.maketrans('', '', string.punctuation)).replace("\n", "")
				if (len(clean_sentence) > 0):
					clean_sentence_array.append(clean_sentence)
		return clean_sentence_array;

dataset = []
for j in range(10):
	print("iteration n°", j)
	for i in range(100):
		dataset = dataset + scrap_random_wiki_page()
		print(i)
	f = open("dataset.json", "a")
	f.write(',\n'.join(dataset))
	f.close()
