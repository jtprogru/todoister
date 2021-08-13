import pytest
from fastapi.testclient import TestClient
from app.main import get_application


@pytest.fixture
def client():
    app = get_application()
    tc = TestClient(app)

    yield tc