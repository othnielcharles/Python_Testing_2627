import server


def test_ne_peut_pas_reserver_plus_de_12_places():
    client = server.app.test_client()

    competition = next(c for c in server.competitions if c["name"] == "Spring Festival")
    places_initiales = int(competition["numberOfPlaces"])

    # Simply Lift a 13 points et Spring Festival a 25 places.
    # On tente d'en réserver 13 (ce qui dépasse la limite autorisée de 12).
    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "13",
        },
    )

    assert int(competition["numberOfPlaces"]) == places_initiales
    assert "12 places" in response.data.decode().lower()
