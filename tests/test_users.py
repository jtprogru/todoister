from tests.conftest import user
import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def default_user_data():
    """Data used during purchase tests. Shortcut just to save typing time"""
    return {
            "username": "kamaz",
            "email": "kamaz@email.com",
            "password": "SuperSecretPassw0rD",
            "registered_datetime": "2041-08-12T00:00:00.000Z"
            }


def test_create_user():
    response = client.post(
        "/api/v1/users/",
        json=default_user_data()
    )

    assert response.status_code == 201
    assert response.json() == {"username": "vasya","email": "vasya@email.com"}

