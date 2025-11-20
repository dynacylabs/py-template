"""
Custom exceptions for the project.
"""


class ProjectError(Exception):
    """Base exception for all project errors."""
    pass


class ConfigurationError(ProjectError):
    """Raised when there's a configuration issue."""
    pass


class ValidationError(ProjectError):
    """Raised when validation fails."""
    pass


class NetworkError(ProjectError):
    """Raised when network operations fail."""
    pass


class NotFoundError(ProjectError):
    """Raised when a resource is not found."""
    pass
