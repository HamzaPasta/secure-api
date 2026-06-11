import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app


@pytest.mark.asyncio
async def test_root_returns_200():
    #Test root endpoint response
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_health_check():
    #Verify health routing and payload structure
    async with AsyncClient(
            transport=ASGITransport(app=app), base_url="http://test"
    ) as client:
        response = await client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"