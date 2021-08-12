import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


# @pytest.fixture


@pytest.fixture
def user(mixer):
    return mixer.blend(
        'app.models.users.User',
        username='vasya',
        email="vasya@email.com",
        password="SuperSecretPassw0rD",
        registered_datetime="2041-08-12T00:00:00.000Z"
    )
