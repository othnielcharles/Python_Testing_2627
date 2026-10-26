import server


def test_reservation_superieure_aux_places_disponibles():
    client = server.app.test_client()

    competition = next(
        c for c in server.competitions
        if c["name"] == "Spring Festival"
    )

    places_initiales = int(competition["numberOfPlaces"])

    client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": str(places_initiales + 1),
        },
    )

    assert int(competition["numberOfPlaces"]) >= 0