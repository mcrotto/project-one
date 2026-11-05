from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_is_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_hello_greets_the_world_by_default() -> None:
    assert client.get("/hello").json() == {"message": "Hello, world!"}


def test_hello_greets_the_given_name() -> None:
    assert client.get("/hello", params={"name": "Ada"}).json() == {"message": "Hello, Ada!"}
