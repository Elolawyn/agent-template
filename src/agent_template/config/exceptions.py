"""Configuration exceptions for agent template."""

from __future__ import annotations


class ConfigurationError(Exception):
    """Exception raised for configuration validation errors."""

    def __init__(self, message: str, field: str | None = None) -> None:
        """Initialize configuration error.

        Args:
            message: Error message describing the validation failure
            field: Optional field name that caused the error
        """
        self.message = message
        self.field = field
        super().__init__(message)
