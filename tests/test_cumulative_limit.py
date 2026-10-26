import server


def test_ne_peut_pas_depasser_12_places_en_cumule():
    client = server.app.test_client()

    competition = next(c for c in server.competitions if c["name"] == "Spring Festival")
    places_initiales = int(competition["numberOfPlaces"])

    # Première réservation valide de 8 places (inférieur à 12)
    response1 = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "8",
        },
    )
    assert int(competition["numberOfPlaces"]) == places_initiales - 8

    # Deuxième réservation de 6 places pour le même club et la même compétition
    # Total = 8 + 6 = 14 > 12 -> doit être refusée
    response2 = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "6",
        },
    )

    # Le nombre de places ne doit pas descendre à places_initiales - 14
    assert int(competition["numberOfPlaces"]) == places_initiales - 8
    assert "12 places" in response2.data.decode().lower()
