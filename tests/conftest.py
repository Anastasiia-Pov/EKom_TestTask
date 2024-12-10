import pytest
from main import app
from beanie import init_beanie
from asgi_lifespan import LifespanManager
from httpx import AsyncClient, ASGITransport
from config import MONGO_DB, MONGO_HOST, MONGO_PORT


DATABASE_URL = f"mongodb://{MONGO_HOST}:{MONGO_PORT}"


@pytest.fixture
async def test_client():
    async with LifespanManager(app):
        async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test", follow_redirects=True) as ac:
            yield ac

