import server


def test_email_inconnu_ne_provoque_pas_erreur():
    client = server.app.test_client()

    response = client.post(
        "/showSummary",
        data={"email": "inconnu@example.com"},
    )

    assert response.status_code == 302