"""
Test configuration and fixtures.
"""

import os
import pytest
import responses as responses_lib
from typing import Dict, Any

from app import Client, HelloWorld


# Test configuration
TEST_BASE_URL = "https://api.example.com"
TEST_TIMEOUT = 30


@pytest.fixture
def hello_world():
    """Create a HelloWorld instance for testing."""
    return HelloWorld()


@pytest.fixture
def hello_world_custom():
    """Create a HelloWorld instance with custom parameters."""
    return HelloWorld(name="Alice", greeting="Hi")


@pytest.fixture
def client():
    """Create a Client instance for testing."""
    return Client(base_url=TEST_BASE_URL, timeout=TEST_TIMEOUT)


@pytest.fixture
def responses():
    """Enable responses mock for HTTP requests."""
    with responses_lib.RequestsMock() as rsps:
        yield rsps


@pytest.fixture
def sample_api_response() -> Dict[str, Any]:
    """Sample API response data for testing."""
    return {
        "status": "success",
        "data": {
            "id": 123,
            "name": "Test Item",
            "description": "A test item"
        }
    }


@pytest.fixture
def sample_error_response() -> Dict[str, Any]:
    """Sample error response data for testing."""
    return {
        "status": "error",
        "message": "Something went wrong"
    }
