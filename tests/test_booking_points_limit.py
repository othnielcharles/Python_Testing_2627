import server


def test_ne_peut_pas_reserver_plus_de_places_que_de_points():
    client = server.app.test_client()

    club = next(c for c in server.clubs if c["name"] == "Iron Temple")
    competition = next(c for c in server.competitions if c["name"] == "Spring Festival")

    points_disponibles = int(club["points"])
    places_initiales_comp = int(competition["numberOfPlaces"])

    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Iron Temple",
            "places": str(points_disponibles + 1),
        },
    )

    assert int(competition["numberOfPlaces"]) == places_initiales_comp
    assert "not enough points" in response.data.decode().lower()
