import pytest
from app.models import User

pytestmark = [
    pytest.mark.freeze_time('2041-08-12 00:00:00'),
]


def test_user_model_instance(mocked_user_model):
    """Проверка что объект является инстансом класса модели"""
    assert isinstance(mocked_user_model, User)


def test_user_username(mocked_user_model, default_user_data):
    """Проверка что username не пустая строка"""
    assert mocked_user_model.username == default_user_data.get("username")
    assert isinstance(mocked_user_model.username, str)
    assert len(mocked_user_model.username) > 0


def test_user_email(mocked_user_model, default_user_data):
    """Проверка email"""
    # TODO: Придумать валидацию Email для теста
    assert '@' in mocked_user_model.email
    assert mocked_user_model.email == default_user_data.get("email")

