import server


def test_competition_inconnue_ne_provoque_pas_index_error():
    client = server.app.test_client()

    response = client.get("/book/CompetitionInconnue/Simply Lift", follow_redirects=True)

    # Ne doit pas lever IndexError (HTTP 500)
    assert response.status_code == 200
    assert "something went wrong" in response.data.decode().lower()


def test_club_inconnu_ne_provoque_pas_index_error():
    client = server.app.test_client()

    response = client.get("/book/Spring Festival/ClubInconnu", follow_redirects=True)

    # Ne doit pas lever IndexError (HTTP 500)
    assert response.status_code == 200
    assert "something went wrong" in response.data.decode().lower()
