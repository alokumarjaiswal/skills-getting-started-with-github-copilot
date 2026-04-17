import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture(scope="module")
def test_client():
    return TestClient(app)
