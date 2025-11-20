"""
Utility functions for the project.
"""

from typing import Any, Dict, List, Optional


def format_dict(data: Dict[str, Any], indent: int = 2) -> str:
    """
    Format a dictionary as a readable string.
    
    Args:
        data: Dictionary to format.
        indent: Number of spaces for indentation.
    
    Returns:
        Formatted string representation.
    
    Example:
        >>> format_dict({"name": "Alice", "age": 30})
        'name: Alice\\nage: 30'
    """
    lines = []
    for key, value in data.items():
        lines.append(f"{key}: {value}")
    return '\n'.join(lines)


def validate_email(email: str) -> bool:
    """
    Simple email validation.
    
    Args:
        email: Email address to validate.
    
    Returns:
        True if email appears valid, False otherwise.
    
    Example:
        >>> validate_email("user@example.com")
        True
        >>> validate_email("invalid-email")
        False
    """
    return '@' in email and '.' in email.split('@')[-1]


def chunk_list(items: List[Any], chunk_size: int) -> List[List[Any]]:
    """
    Split a list into chunks of specified size.
    
    Args:
        items: List to chunk.
        chunk_size: Size of each chunk.
    
    Returns:
        List of chunked lists.
    
    Example:
        >>> chunk_list([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
    """
    return [items[i:i + chunk_size] for i in range(0, len(items), chunk_size)]
