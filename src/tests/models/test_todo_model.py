import pytest
from app.models import Todo

pytestmark = [
    pytest.mark.freeze_time("2041-08-12T00:00:00.000Z"),
]


def test_todo_model_instance(mocked_todo_model):
    """Проверка что объект является инстансом класса модели"""
    assert isinstance(mocked_todo_model, Todo)


def test_todo_title(mocked_todo_model, default_todo_data):
    """Проверка что title не пустая строка"""
    assert mocked_todo_model.title == default_todo_data.get("title")
    assert isinstance(mocked_todo_model.title, str)
    assert len(mocked_todo_model.title) > 0


def test_todo_description(mocked_todo_model, default_todo_data):
    """Проверка description"""
    assert mocked_todo_model.description == default_todo_data.get("description")
    assert isinstance(mocked_todo_model.description, str)
    assert len(mocked_todo_model.description) > 0


def test_todo_created_datetime(mocked_todo_model, default_todo_data):
    """Проверка корректности и наличия даты создания таски"""
    assert mocked_todo_model.created_datetime == "2041-08-12T00:00:00.000Z"
