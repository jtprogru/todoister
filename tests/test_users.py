import pytest
from app.models import User


@pytest.mark.xfail
def test_get_users_list(client):
    """Получение списка всех пользователей"""
    response = client.get("/api/v1/users")

    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_user_model(mocked_user_model):
    user_model = mocked_user_model

    assert user_model.id == 1
    assert user_model.username == "kamaz"
    assert user_model.email == "kamaz@email.com"
    assert user_model.registered_datetime == "2041-08-12T00:00:00.000Z"
    assert user_model.is_superuser is False
    assert isinstance(user_model, User)
