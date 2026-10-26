import server


def test_points_sont_deduits_apres_reservation():
    client = server.app.test_client()

    club = next(
        c for c in server.clubs
        if c["name"] == "Simply Lift"
    )
    points_initiaux = int(club["points"])
    places_a_reserver = 2

    client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": str(places_a_reserver),
        },
    )

    assert int(club["points"]) == points_initiaux - places_a_reserver
