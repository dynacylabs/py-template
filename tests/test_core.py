"""
Tests for core functionality.
"""

import pytest
from app import HelloWorld
from app.core import add_numbers, multiply_numbers


@pytest.mark.unit
class TestHelloWorld:
    """Test the HelloWorld class."""
    
    def test_init_default(self):
        """Test default initialization."""
        hw = HelloWorld()
        assert hw.name == "World"
        assert hw.greeting == "Hello"
    
    def test_init_custom(self):
        """Test initialization with custom parameters."""
        hw = HelloWorld(name="Alice", greeting="Hi")
        assert hw.name == "Alice"
        assert hw.greeting == "Hi"
    
    def test_greet_default(self, hello_world):
        """Test default greeting."""
        result = hello_world.greet()
        assert result == "Hello, World!"
    
    def test_greet_custom(self, hello_world_custom):
        """Test custom greeting."""
        result = hello_world_custom.greet()
        assert result == "Hi, Alice!"
    
    def test_greet_multiple(self, hello_world):
        """Test greeting multiple names."""
        names = ["Alice", "Bob", "Charlie"]
        results = hello_world.greet_multiple(names)
        
        assert len(results) == 3
        assert results[0] == "Hello, Alice!"
        assert results[1] == "Hello, Bob!"
        assert results[2] == "Hello, Charlie!"
    
    def test_greet_multiple_empty_list(self, hello_world):
        """Test greeting with empty list."""
        results = hello_world.greet_multiple([])
        assert results == []
    
    def test_set_greeting(self, hello_world):
        """Test updating the greeting."""
        hello_world.set_greeting("Howdy")
        assert hello_world.greeting == "Howdy"
        assert hello_world.greet() == "Howdy, World!"
    
    def test_set_name(self, hello_world):
        """Test updating the name."""
        hello_world.set_name("Bob")
        assert hello_world.name == "Bob"
        assert hello_world.greet() == "Hello, Bob!"
    
    def test_chained_updates(self, hello_world):
        """Test multiple updates."""
        hello_world.set_name("Alice")
        hello_world.set_greeting("Hey")
        assert hello_world.greet() == "Hey, Alice!"


@pytest.mark.unit
class TestMathFunctions:
    """Test mathematical utility functions."""
    
    def test_add_numbers_integers(self):
        """Test adding integers."""
        result = add_numbers(2, 3)
        assert result == 5.0
    
    def test_add_numbers_floats(self):
        """Test adding floats."""
        result = add_numbers(1.5, 2.5)
        assert result == 4.0
    
    def test_add_numbers_negative(self):
        """Test adding negative numbers."""
        result = add_numbers(-5, 3)
        assert result == -2.0
    
    def test_add_numbers_zero(self):
        """Test adding zero."""
        result = add_numbers(10, 0)
        assert result == 10.0
    
    def test_multiply_numbers_integers(self):
        """Test multiplying integers."""
        result = multiply_numbers(2, 3)
        assert result == 6.0
    
    def test_multiply_numbers_floats(self):
        """Test multiplying floats."""
        result = multiply_numbers(1.5, 2)
        assert result == 3.0
    
    def test_multiply_numbers_negative(self):
        """Test multiplying negative numbers."""
        result = multiply_numbers(-2, 3)
        assert result == -6.0
    
    def test_multiply_numbers_zero(self):
        """Test multiplying by zero."""
        result = multiply_numbers(5, 0)
        assert result == 0.0
