"""
Tests for custom exceptions.
"""

import pytest
from app.exceptions import (
    ProjectError,
    ConfigurationError,
    ValidationError,
    NetworkError,
    NotFoundError,
)


@pytest.mark.unit
class TestExceptions:
    """Test custom exceptions."""
    
    def test_project_error(self):
        """Test base ProjectError exception."""
        with pytest.raises(ProjectError) as exc_info:
            raise ProjectError("Test error")
        
        assert "Test error" in str(exc_info.value)
    
    def test_configuration_error(self):
        """Test ConfigurationError exception."""
        with pytest.raises(ConfigurationError) as exc_info:
            raise ConfigurationError("Configuration issue")
        
        assert "Configuration issue" in str(exc_info.value)
        assert isinstance(exc_info.value, ProjectError)
    
    def test_validation_error(self):
        """Test ValidationError exception."""
        with pytest.raises(ValidationError) as exc_info:
            raise ValidationError("Validation failed")
        
        assert "Validation failed" in str(exc_info.value)
        assert isinstance(exc_info.value, ProjectError)
    
    def test_network_error(self):
        """Test NetworkError exception."""
        with pytest.raises(NetworkError) as exc_info:
            raise NetworkError("Network issue")
        
        assert "Network issue" in str(exc_info.value)
        assert isinstance(exc_info.value, ProjectError)
    
    def test_not_found_error(self):
        """Test NotFoundError exception."""
        with pytest.raises(NotFoundError) as exc_info:
            raise NotFoundError("Resource not found")
        
        assert "Resource not found" in str(exc_info.value)
        assert isinstance(exc_info.value, ProjectError)
