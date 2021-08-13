import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core import Base as TestBase
from app.main import app
from app.services import get_db
from app import models

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.sqlite"

test_engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)


TestBase.metadata.create_all(bind=test_engine)


def override_get_db():
    try:
        test_db = TestingSessionLocal()
        yield test_db
    finally:
        test_db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    tc = TestClient(app)

    yield tc


@pytest.fixture
def default_user_data():
    """Default user for testing"""
    return {
        "username": "kamaz",
        "email": "kamaz@email.com",
        "password": "SuperSecretPassw0rD",
        "registered_datetime": "2041-08-12T00:00:00.000Z"
    }


@pytest.fixture
def mocked_user_model():
    user = models.User(
        id=1,
        username="kamaz",
        email="kamaz@email.com",
        password="SuperSecretPassw0rD",
        registered_datetime="2041-08-12T00:00:00.000Z",
        is_superuser=False
    )
    return user
