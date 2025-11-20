"""
Package initialization tests.
"""

import pytest
import app


@pytest.mark.unit
class TestPackageInit:
    """Test package initialization."""
    
    def test_version_exists(self):
        """Test that version is defined."""
        assert hasattr(app, '__version__')
        assert isinstance(app.__version__, str)
    
    def test_exports(self):
        """Test that expected classes are exported."""
        assert hasattr(app, 'Client')
        assert hasattr(app, 'HelloWorld')
        assert hasattr(app, 'ProjectError')
        assert hasattr(app, 'ConfigurationError')
        assert hasattr(app, 'ValidationError')
    
    def test_all_attribute(self):
        """Test __all__ is defined and contains expected items."""
        assert hasattr(app, '__all__')
        assert 'Client' in app.__all__
        assert 'HelloWorld' in app.__all__
