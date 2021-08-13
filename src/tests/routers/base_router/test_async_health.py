import pytest
from httpx import AsyncClient

from app.main import app


@pytest.mark.asyncio
async def test_async_get_healthcheck():
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8089") as ac:
        response = await ac.get("/api/v1/healthcheck")
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}


@pytest.mark.asyncio
async def test_get_healthcheck_error(client):
    async with AsyncClient(app=app, base_url="http://127.0.0.1:8089") as ac:
        response = await ac.get("/api/v1/healthchec")
    assert response.status_code == 404
