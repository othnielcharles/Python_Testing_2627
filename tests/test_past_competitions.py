import server


def test_competition_passee_ne_peut_pas_etre_ouverte():
    client = server.app.test_client()

    response = client.get(
        "/book/Spring Festival/Simply Lift"
    )

    assert response.status_code == 302


def test_competition_passee_ne_doit_pas_accepter_de_reservation():
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
            "places": "1",
        },
    )

    assert int(competition["numberOfPlaces"]) == places_initiales