import server


def test_tableau_des_points_accessible_publiquement():
    client = server.app.test_client()

    response = client.get("/points")

    # La route doit répondre avec succès (200) sans nécessiter de connexion
    assert response.status_code == 200

    html = response.data.decode()
    # Tous les clubs doivent figurer dans le tableau public avec leurs points
    for club in server.clubs:
        assert club["name"] in html
        assert str(club["points"]) in html
