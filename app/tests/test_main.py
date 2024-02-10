from fastapi.testclient import TestClient

from app.api.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/api")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_invalid_data():
    data = {"age": 20}
    response = client.post("/api/human_age", json=data)
    assert response.status_code == 422


def test_valid_data():
    data = {"name": "Alice"}
    response = client.post("/api/human_age", json=data)
    assert response.status_code == 200


def test_cached_response():
    data = {"name": "John"}
    response = client.post("/api/human_age", json=data)
    assert response.status_code == 200
    responseData = response.json()

    response = client.post("/api/human_age", json=data)
    assert response.json() == responseData
