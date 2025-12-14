"""Configuration management system for agent template."""

from __future__ import annotations

from .manager import (
    ConfigurationError,
    ConfigurationManager,
    Settings,
    config_manager,
)

__all__ = [
    "ConfigurationError",
    "ConfigurationManager",
    "Settings",
    "config_manager",
]
