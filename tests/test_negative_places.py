import server


def test_ne_peut_pas_reserver_nombre_negatif_de_places():
    client = server.app.test_client()

    competition = next(c for c in server.competitions if c["name"] == "Spring Festival")
    places_initiales = int(competition["numberOfPlaces"])

    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "-4",
        },
    )

    # Le nombre de places ne doit pas augmenter (25 - (-4) = 29)
    assert int(competition["numberOfPlaces"]) == places_initiales
    assert "at least 1 place" in response.data.decode().lower() or "invalid" in response.data.decode().lower()


def test_ne_peut_pas_reserver_zero_place():
    client = server.app.test_client()

    competition = next(c for c in server.competitions if c["name"] == "Spring Festival")
    places_initiales = int(competition["numberOfPlaces"])

    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "0",
        },
    )

    assert int(competition["numberOfPlaces"]) == places_initiales
    assert "at least 1 place" in response.data.decode().lower() or "invalid" in response.data.decode().lower()
