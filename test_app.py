from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_add():
    client = app.test_client()

    response = client.get("/add/10/5")

    assert response.status_code == 200
    assert response.json["result"] == 15