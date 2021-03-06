import pytest


def test_get_healthcheck(client):
    response = client.get("/api/v1/healthcheck")

    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


def test_healthcheck_error(client):
    response = client.get("/api/v1/healthchec")

    assert response.status_code == 404
