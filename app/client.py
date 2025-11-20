"""
HTTP client for making external requests.
"""

import requests
from typing import Dict, Any, Optional
from .exceptions import NetworkError, NotFoundError


class Client:
    """
    A simple HTTP client wrapper.
    
    Args:
        base_url: Base URL for API requests.
        timeout: Request timeout in seconds. Defaults to 30.
        headers: Optional custom headers to include in all requests.
    
    Example:
        >>> client = Client(base_url="https://api.example.com")
        >>> data = client.get("/endpoint")
    """
    
    def __init__(
        self,
        base_url: str = "",
        timeout: int = 30,
        headers: Optional[Dict[str, str]] = None
    ):
        """Initialize the HTTP client."""
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.headers = headers or {}
        self.session = requests.Session()
        self.session.headers.update(self.headers)
    
    def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Make a GET request.
        
        Args:
            endpoint: API endpoint path.
            params: Optional query parameters.
        
        Returns:
            JSON response as dictionary.
        
        Raises:
            NetworkError: If the request fails.
            NotFoundError: If the resource is not found (404).
        """
        url = f"{self.base_url}{endpoint}" if self.base_url else endpoint
        
        try:
            response = self.session.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                raise NotFoundError(f"Resource not found: {url}")
            raise NetworkError(f"HTTP error occurred: {e}")
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error occurred: {e}")
    
    def post(
        self,
        endpoint: str,
        data: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Make a POST request.
        
        Args:
            endpoint: API endpoint path.
            data: Optional form data.
            json: Optional JSON data.
        
        Returns:
            JSON response as dictionary.
        
        Raises:
            NetworkError: If the request fails.
        """
        url = f"{self.base_url}{endpoint}" if self.base_url else endpoint
        
        try:
            response = self.session.post(
                url,
                data=data,
                json=json,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise NetworkError(f"Network error occurred: {e}")
    
    def close(self) -> None:
        """Close the session."""
        self.session.close()
    
    def __enter__(self):
        """Context manager entry."""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()
