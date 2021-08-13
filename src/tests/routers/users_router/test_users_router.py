import pytest


def test_get_users_list(client):
    """Получение списка всех пользователей"""
    response = client.get("/api/v1/users/")

    assert isinstance(response.json(), list)
    assert response.json() == []
    assert response.status_code == 200


@pytest.mark.xfail
def test_create_user(client, default_user_data):
    response = client.post("/api/v1/users/", data=default_user_data)

    # assert response.status_code == 201
    assert response.json() == {
        "username": "kamaz",
        "email": "kamaz@email.com",
    }
