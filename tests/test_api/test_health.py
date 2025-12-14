"""Tests for health endpoint."""

from fastapi.testclient import TestClient


def test_health_endpoint_v1(client: TestClient) -> None:
    """Test the health check endpoint at /api/v1/health/."""
    response = client.get("/api/v1/health/")

    assert response.status_code == 200
    data = response.json()

    assert "name" in data
    assert "description" in data
    assert "version" in data
    assert "status" in data
    assert data["status"] == "healthy"
    # Check that name comes from dynamic metadata
    from agent_template._metadata import get_api_metadata

    expected_name = get_api_metadata()["api_title"]
    assert data["name"] == expected_name
    assert data["status"] == "healthy"


def test_health_endpoint_root(client: TestClient) -> None:
    """Test health check endpoint at root (/)."""
    response = client.get("/")

    assert response.status_code == 200
    data = response.json()

    # Should return same data as v1 endpoint
    assert "name" in data
    assert "description" in data
    assert "version" in data
    assert "status" in data
    assert data["status"] == "healthy"

    # Check that name comes from dynamic metadata
    from agent_template._metadata import get_api_metadata

    expected_name = get_api_metadata()["api_title"]
    assert data["name"] == expected_name


def test_health_endpoints_consistency(client: TestClient) -> None:
    """Test that both health endpoints return consistent data."""
    v1_response = client.get("/api/v1/health/")
    root_response = client.get("/")

    assert v1_response.status_code == 200
    assert root_response.status_code == 200

    v1_data = v1_response.json()
    root_data = root_response.json()

    # Both endpoints should return identical data
    assert v1_data == root_data
