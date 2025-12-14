"""Pytest configuration and fixtures."""

import os
from collections.abc import Generator

import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient

from agent_template.app import create_app
from tests.test_settings import TestSettings


@pytest.fixture(autouse=True)
def clean_environment() -> Generator[None]:
    """Clean environment variables before each test to prevent contamination."""
    # Store original environment variables that might affect tests
    original_env: dict[str, str] = {}
    env_vars_to_clean = [
        "ENVIRONMENT",
        "DEBUG",
        "HOST",
        "PORT",
        "API_TITLE",
        "API_DESCRIPTION",
        "API_VERSION",
        "LOG_LEVEL",
    ]

    for var in env_vars_to_clean:
        if var in os.environ:
            original_env[var] = os.environ[var]
            del os.environ[var]

    yield

    # Restore original environment variables
    for var, value in original_env.items():
        os.environ[var] = value


@pytest.fixture
def test_settings() -> TestSettings:
    """Create test settings for the application."""
    return TestSettings()


@pytest.fixture
def client(test_settings: TestSettings) -> Generator[TestClient]:
    """Create a test client for the FastAPI app with test settings."""
    app = create_app(test_settings)
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture
def app(test_settings: TestSettings) -> Generator[FastAPI]:
    """Create a FastAPI app instance for testing."""
    app = create_app(test_settings)
    yield app
