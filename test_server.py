# test_main.py
from fastapi.testclient import TestClient
import logging
from httpx import AsyncClient
from typing import AsyncIterable
import pytest

_URL: str = "http://127.0.0.1:8000"
_logger = logging.getLogger(__name__)

@pytest.fixture
async def client() -> AsyncIterable[AsyncClient]:
    client = AsyncClient(base_url=_URL)
    yield client

async def test_read_root(client):
    async with client.stream("GET", "/") as response:
        async for line in response.aiter_lines():
            _logger.info(line)