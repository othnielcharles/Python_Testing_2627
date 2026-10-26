import server


def test_concours_complet_affiche_message_et_bloque_reservation():
    client = server.app.test_client()

    competition = next(c for c in server.competitions if c["name"] == "Spring Festival")
    places_sauvegardees = competition["numberOfPlaces"]
    competition["numberOfPlaces"] = "0"

    try:
        # 1. Tentative d'accès à la page de réservation d'un concours complet
        response_book = client.get("/book/Spring Festival/Simply Lift", follow_redirects=True)
        assert "competition is full" in response_book.data.decode().lower()

        # 2. Tentative de réservation directe par POST
        response_purchase = client.post(
            "/purchasePlaces",
            data={
                "competition": "Spring Festival",
                "club": "Simply Lift",
                "places": "1",
            },
            follow_redirects=True,
        )
        assert int(competition["numberOfPlaces"]) == 0
        assert "competition is full" in response_purchase.data.decode().lower()
    finally:
        competition["numberOfPlaces"] = places_sauvegardees
