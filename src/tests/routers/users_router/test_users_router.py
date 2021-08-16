"""Модуль тестирования роутера users."""


def test_get_users_list(client, status_code_ok):
    """Тестирование получения списка всех пользователей.

    Args:
        client: pytest fixture
        status_code_ok: 200 OK status code
    """
    response = client.get('/api/v1/users/')
    assert isinstance(response.json(), list)
    assert response.status_code == status_code_ok


def test_create_user(mocked_user_create, default_user_data, status_code_ok):
    """Тестирование создания пользователя.

    Args:
        mocked_user_create: pytest fixture
        default_user_data: pytest fixture
        status_code_ok: 200 OK status code
    """
    response = mocked_user_create

    assert response.status_code == status_code_ok
    assert response.json() == {
        "username": "kamaz",
        "email": "kamaz@email.com",
    }
