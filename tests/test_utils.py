"""
Tests for utility functions.
"""

import pytest
from app.utils import format_dict, validate_email, chunk_list


@pytest.mark.unit
class TestFormatDict:
    """Test format_dict function."""
    
    def test_format_dict_simple(self):
        """Test formatting a simple dictionary."""
        data = {"name": "Alice", "age": 30}
        result = format_dict(data)
        assert "name: Alice" in result
        assert "age: 30" in result
    
    def test_format_dict_empty(self):
        """Test formatting an empty dictionary."""
        result = format_dict({})
        assert result == ""
    
    def test_format_dict_single_item(self):
        """Test formatting a single-item dictionary."""
        result = format_dict({"key": "value"})
        assert result == "key: value"


@pytest.mark.unit
class TestValidateEmail:
    """Test validate_email function."""
    
    def test_validate_email_valid(self):
        """Test validation of valid email addresses."""
        assert validate_email("user@example.com") is True
        assert validate_email("test.user@domain.co.uk") is True
        assert validate_email("name+tag@example.org") is True
    
    def test_validate_email_invalid(self):
        """Test validation of invalid email addresses."""
        assert validate_email("invalid-email") is False
        assert validate_email("@example.com") is False
        assert validate_email("user@") is False
        assert validate_email("user") is False
    
    def test_validate_email_edge_cases(self):
        """Test edge cases."""
        assert validate_email("a@b.c") is True
        assert validate_email("") is False


@pytest.mark.unit
class TestChunkList:
    """Test chunk_list function."""
    
    def test_chunk_list_even_split(self):
        """Test chunking with even split."""
        items = [1, 2, 3, 4, 5, 6]
        result = chunk_list(items, 2)
        assert result == [[1, 2], [3, 4], [5, 6]]
    
    def test_chunk_list_uneven_split(self):
        """Test chunking with uneven split."""
        items = [1, 2, 3, 4, 5]
        result = chunk_list(items, 2)
        assert result == [[1, 2], [3, 4], [5]]
    
    def test_chunk_list_single_chunk(self):
        """Test chunking into single chunk."""
        items = [1, 2, 3]
        result = chunk_list(items, 10)
        assert result == [[1, 2, 3]]
    
    def test_chunk_list_empty(self):
        """Test chunking empty list."""
        result = chunk_list([], 2)
        assert result == []
    
    def test_chunk_list_size_one(self):
        """Test chunking with size 1."""
        items = [1, 2, 3]
        result = chunk_list(items, 1)
        assert result == [[1], [2], [3]]
