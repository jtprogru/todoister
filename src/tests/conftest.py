import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.models.todos import Todo
from app.models.users import User
from app.core import Base
from app.main import app
from app.services import db_services

SQLALCHEMY_DATABASE_URL = "sqlite:////tmp/test.sqlite"

test_engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


@pytest.fixture(autouse=True)
def prepare_and_cleaning_env():
    Base.metadata.create_all(bind=test_engine)

    def override_get_db():
        try:
            test_db = TestingSessionLocal()
            yield test_db
        finally:
            test_db.close()

    app.dependency_overrides[db_services.get_db] = override_get_db

    yield

    if os.path.exists("/tmp/test.sqlite"):
        os.remove("/tmp/test.sqlite")
    else:
        print("Can not delete the file as it doesn't exists")


@pytest.fixture
def default_user_data():
    """Словарь с данными пользователя поумолчанию"""
    return {
        "username": "kamaz",
        "email": "kamaz@email.com",
        "password": "SuperSecretPassw0rD",
    }


@pytest.fixture
def default_todo_data():
    """Словарь с данными пользователя поумолчанию"""
    return {"title": "Молоко", "description": "Купить молоко в Ашане 200 литров", "created_datetime": "2041-08-12T00:00:00.000Z"}


@pytest.fixture
def mocked_user_model(default_user_data):
    """Обект модели User с данными поумолчанию"""
    return User(
        id=1,
        username=default_user_data.get("username"),
        email=default_user_data.get("email"),
        password=default_user_data.get("password"),
        registered_datetime=default_user_data.get("registered_datetime"),
        is_superuser=False,
    )


@pytest.fixture
def mocked_todo_model(default_todo_data):
    """Обект модели Todo с данными поумолчанию"""
    return Todo(
        id=1,
        title=default_todo_data.get("title"),
        description=default_todo_data.get("description"),
        created_datetime=default_todo_data.get("created_datetime")
        # owner_id = Column(Integer, ForeignKey("users_router.id"))
        # owner = relationship("User", back_populates="todos")
    )
