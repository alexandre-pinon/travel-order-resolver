def generate_data():
    starts = [
        "Je veux savoir", "Je souhaite savoir", "J'aimerais savoir",
        "Je voudrais savoir", "Puis-je savoir", "Dis-moi", "Saurais-tu",
        "Tu sais", "Indique-moi", "Sais-tu", "Tu saurais"
    ]

    hows = [
        "comment", "comment faire pour",
        "quel est le meilleur itinéraire pour",
        "quel est le meilleur trajet pour"
    ]

    middles = [
        "aller",
        "arriver",
        "partir",
        "faire route",
        "me rendre",
        "me diriger",
        "se rendre",
        "se diriger",
    ]

    joins = ["à", "vers"]
    departure = "{{DEPARTURE}}"
    arrival = "{{ARRIVAL}}"

    ends = ["depuis", "en partant de"]

    # Je veux savoir comment aller à {{ARRIVAL}} depuis {{DEPARTURE}}...
    data = [
        f"{start} {how} {middle} {join} {arrival} {end} {departure}"
        for start in starts for how in hows for middle in middles
        for join in joins for end in ends
    ]

    starts = ["Je veux", "Je souhaite", "J'aimerais", "Je voudrais"]
    middles_me = middles[:-2]

    # Je veux aller de {{ARRIVAL}} à {{DEPARTURE}}...
    data += [
        f"{start} {middle} de {arrival} {join} {departure}" for start in starts
        for middle in middles_me for join in joins
    ]
    # Comment aller de {{ARRIVAL}} à {{DEPARTURE}}...
    data += [
        f"{how.capitalize()} {middle} de {arrival} {join} {departure}"
        for how in hows for middle in middles for join in joins
    ]

    # Depuis {{DEPARTURE}} je veux aller à {{ARRIVAL}}...
    data += [
        f"{end.capitalize()} {departure} {start.lower()} {middle} {join} {arrival}"
        for end in ends for start in starts for middle in middles_me
        for join in joins
    ]
    # Depuis {{DEPARTURE}} comment aller à {{ARRIVAL}}...
    data += [
        f"{end.capitalize()} {departure} {how} {middle} {join} {arrival}"
        for end in ends for how in hows for middle in middles_me
        for join in joins
    ]

    starts = [
        "Aller à", "Aller vers", "Aller voir", "Direction", "Destination",
        "Partir en direction de", "Découvrir", "Trajet direction",
        "Donne-moi un trajet en direction de"
    ]
    ends.append("de")

    # Aller à {{ARRIVAL}} depuis {{DEPARTURE}}...
    data += [
        f"{start} {arrival} {end} {departure}" for start in starts
        for end in ends
    ]

    uniques = [
        f"Donne-moi un trajet entre {departure} et {arrival}",
        f"Quel est le trajet {departure}-{arrival}",
        f"Départ {departure} arrivée {arrival}",
        f"De {departure} aller à {arrival}",
        f"De {departure} aller vers {arrival}",
        f"Depuis {departure} aller à {arrival}",
        f"Depuis {departure} aller vers {arrival}",
    ]

    data += uniques

    with open('travel_order_data.csv', 'w') as f:
        f.write("\n".join(data))


if __name__ == "__main__":
    generate_data()
