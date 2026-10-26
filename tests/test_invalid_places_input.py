import server


def test_champ_places_vide_ne_leve_pas_value_error():
    client = server.app.test_client()

    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "",
        },
        follow_redirects=True,
    )

    # Ne doit pas lever ValueError (HTTP 500)
    assert response.status_code == 200
    assert "valid" in response.data.decode().lower() or "invalid" in response.data.decode().lower()


def test_champ_places_texte_ne_leve_pas_value_error():
    client = server.app.test_client()

    response = client.post(
        "/purchasePlaces",
        data={
            "competition": "Spring Festival",
            "club": "Simply Lift",
            "places": "deux",
        },
        follow_redirects=True,
    )

    # Ne doit pas lever ValueError (HTTP 500)
    assert response.status_code == 200
    assert "valid" in response.data.decode().lower() or "invalid" in response.data.decode().lower()
