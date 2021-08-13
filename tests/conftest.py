import pytest
from _pytest import monkeypatch
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture
def client():
    mp = monkeypatch.MonkeyPatch()
    mp.setenv('DATABASE_URI', 'sqlite:///./test.sqlite')
    client = TestClient(app)

    yield client
