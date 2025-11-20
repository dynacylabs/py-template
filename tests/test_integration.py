"""
Integration tests.

These tests may require external services or configurations.
Mark them with @pytest.mark.integration to skip during fast test runs.
"""

import pytest
from app import HelloWorld


@pytest.mark.integration
class TestIntegration:
    """Integration tests."""
    
    def test_basic_integration(self):
        """Test basic integration scenario."""
        hw = HelloWorld(name="Integration Test")
        result = hw.greet()
        assert "Integration Test" in result
    
    @pytest.mark.slow
    def test_slow_operation(self):
        """Test a slow operation."""
        # Simulate a slow operation
        hw = HelloWorld()
        names = [f"User{i}" for i in range(100)]
        results = hw.greet_multiple(names)
        assert len(results) == 100
