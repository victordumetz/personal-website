"""Test the main module."""

from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_index():
    """Test getting the index."""
    response = client.get("/")
    assert response.status_code == status.HTTP_200_OK
