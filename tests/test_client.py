"""
Tests for the HTTP client.
"""

import pytest
import responses as responses_lib
from app import Client
from app.exceptions import NetworkError, NotFoundError


@pytest.mark.unit
class TestClientInitialization:
    """Test Client class initialization."""
    
    def test_init_with_base_url(self):
        """Test initialization with base URL."""
        client = Client(base_url="https://api.example.com")
        assert client.base_url == "https://api.example.com"
        assert client.timeout == 30
    
    def test_init_with_trailing_slash(self):
        """Test that trailing slash is removed from base URL."""
        client = Client(base_url="https://api.example.com/")
        assert client.base_url == "https://api.example.com"
    
    def test_init_custom_timeout(self):
        """Test initialization with custom timeout."""
        client = Client(timeout=60)
        assert client.timeout == 60
    
    def test_init_custom_headers(self):
        """Test initialization with custom headers."""
        headers = {"Authorization": "Bearer token123"}
        client = Client(headers=headers)
        assert "Authorization" in client.headers


@pytest.mark.unit
class TestClientGet:
    """Test GET requests."""
    
    @responses_lib.activate
    def test_get_success(self, client, sample_api_response):
        """Test successful GET request."""
        responses_lib.add(
            responses_lib.GET,
            f"{client.base_url}/test",
            json=sample_api_response,
            status=200
        )
        
        result = client.get("/test")
        assert result == sample_api_response
    
    @responses_lib.activate
    def test_get_with_params(self, client, sample_api_response):
        """Test GET request with query parameters."""
        responses_lib.add(
            responses_lib.GET,
            f"{client.base_url}/test",
            json=sample_api_response,
            status=200
        )
        
        params = {"page": 1, "limit": 10}
        result = client.get("/test", params=params)
        assert result == sample_api_response
    
    @responses_lib.activate
    def test_get_not_found(self, client):
        """Test GET request returning 404."""
        responses_lib.add(
            responses_lib.GET,
            f"{client.base_url}/notfound",
            json={"error": "Not found"},
            status=404
        )
        
        with pytest.raises(NotFoundError) as exc_info:
            client.get("/notfound")
        
        assert "Resource not found" in str(exc_info.value)
    
    @responses_lib.activate
    def test_get_server_error(self, client):
        """Test GET request returning 500."""
        responses_lib.add(
            responses_lib.GET,
            f"{client.base_url}/error",
            json={"error": "Server error"},
            status=500
        )
        
        with pytest.raises(NetworkError) as exc_info:
            client.get("/error")
        
        assert "HTTP error" in str(exc_info.value)


@pytest.mark.unit
class TestClientPost:
    """Test POST requests."""
    
    @responses_lib.activate
    def test_post_success(self, client, sample_api_response):
        """Test successful POST request."""
        responses_lib.add(
            responses_lib.POST,
            f"{client.base_url}/test",
            json=sample_api_response,
            status=200
        )
        
        data = {"name": "Test"}
        result = client.post("/test", json=data)
        assert result == sample_api_response
    
    @responses_lib.activate
    def test_post_with_json(self, client, sample_api_response):
        """Test POST request with JSON data."""
        responses_lib.add(
            responses_lib.POST,
            f"{client.base_url}/create",
            json=sample_api_response,
            status=201
        )
        
        json_data = {"key": "value"}
        result = client.post("/create", json=json_data)
        assert result == sample_api_response
    
    @responses_lib.activate
    def test_post_error(self, client):
        """Test POST request with error."""
        responses_lib.add(
            responses_lib.POST,
            f"{client.base_url}/error",
            json={"error": "Bad request"},
            status=400
        )
        
        with pytest.raises(NetworkError):
            client.post("/error", json={"data": "test"})


@pytest.mark.unit
class TestClientContextManager:
    """Test Client as context manager."""
    
    def test_context_manager(self):
        """Test using client as context manager."""
        with Client(base_url="https://api.example.com") as client:
            assert client.base_url == "https://api.example.com"
        
        # Session should be closed after exiting context
        assert client.session is not None
