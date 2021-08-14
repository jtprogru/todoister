import pytest
import requests_mock


def test_get_users_list(client):
    """Получение списка всех пользователей"""
    response = client.get("/api/v1/users/")
    assert isinstance(response.json(), list)
    assert response.json() == []
    assert response.status_code == 200


def test_create_user(mocked_user_create, default_user_data):
    response = mocked_user_create

    assert response.status_code == 200
    assert response.json() == {
        "username": "kamaz",
        "email": "kamaz@email.com",
    }
