"""
Core functionality module.
"""

from typing import List, Optional


class HelloWorld:
    """
    A simple Hello World class demonstrating basic functionality.
    
    Args:
        name: Optional name to greet. Defaults to "World".
        greeting: Optional custom greeting. Defaults to "Hello".
    
    Example:
        >>> hw = HelloWorld(name="Alice")
        >>> hw.greet()
        'Hello, Alice!'
        
        >>> hw = HelloWorld(name="Bob", greeting="Hi")
        >>> hw.greet()
        'Hi, Bob!'
    """
    
    def __init__(self, name: str = "World", greeting: str = "Hello"):
        """Initialize the HelloWorld instance."""
        self.name = name
        self.greeting = greeting
    
    def greet(self) -> str:
        """
        Return a greeting message.
        
        Returns:
            A formatted greeting string.
        """
        return f"{self.greeting}, {self.name}!"
    
    def greet_multiple(self, names: List[str]) -> List[str]:
        """
        Generate greetings for multiple names.
        
        Args:
            names: List of names to greet.
        
        Returns:
            List of greeting strings.
        """
        return [f"{self.greeting}, {name}!" for name in names]
    
    def set_greeting(self, greeting: str) -> None:
        """
        Update the greeting message.
        
        Args:
            greeting: New greeting to use.
        """
        self.greeting = greeting
    
    def set_name(self, name: str) -> None:
        """
        Update the name to greet.
        
        Args:
            name: New name to greet.
        """
        self.name = name


def add_numbers(a: float, b: float) -> float:
    """
    Add two numbers together.
    
    Args:
        a: First number.
        b: Second number.
    
    Returns:
        Sum of a and b.
    
    Example:
        >>> add_numbers(2, 3)
        5.0
        >>> add_numbers(1.5, 2.5)
        4.0
    """
    return a + b


def multiply_numbers(a: float, b: float) -> float:
    """
    Multiply two numbers.
    
    Args:
        a: First number.
        b: Second number.
    
    Returns:
        Product of a and b.
    
    Example:
        >>> multiply_numbers(2, 3)
        6.0
        >>> multiply_numbers(1.5, 2)
        3.0
    """
    return a * b
