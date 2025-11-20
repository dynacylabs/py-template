"""
Python Project Template

A simple, well-structured Python project with best practices.
"""

__version__ = "0.1.0"

from .client import Client
from .core import HelloWorld
from .exceptions import (
    ProjectError,
    ConfigurationError,
    ValidationError,
)

__all__ = [
    "Client",
    "HelloWorld",
    "ProjectError",
    "ConfigurationError",
    "ValidationError",
]
