import pytest
from fastapi.testclient import TestClient
from app.main import get_application
import pytest
import requests
import requests_mock


@pytest.fixture
def mocked_user_create(requests_mock, default_user_data):
    requests_mock.register_uri(
        "POST",
        "http://127.0.0.1:8089/api/v1/users/",
        text='{"username": "kamaz","email": "kamaz@email.com"}',
    )
    return requests.post("http://127.0.0.1:8089/api/v1/users/", data=default_user_data)


@pytest.fixture
def client():
    app = get_application()
    tc = TestClient(app)

    yield tc
