"""Base configuration settings for agent template."""

from __future__ import annotations

from typing import Any

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

from agent_template._metadata import get_api_metadata


class Settings(BaseSettings):
    """Application settings with validation."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="forbid",
    )

    # Server configuration
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    reload: bool = False

    # API configuration - now sourced from pyproject.toml
    api_title: str = Field(default_factory=lambda: get_api_metadata()["api_title"])
    api_description: str = Field(
        default_factory=lambda: get_api_metadata()["api_description"]
    )
    api_version: str = Field(default_factory=lambda: get_api_metadata()["api_version"])

    # Logging configuration
    log_level: str = "INFO"

    # Environment
    environment: str = "development"

    @property
    def is_testing(self) -> bool:
        """Check if running in testing environment."""
        return self.environment == "testing"

    @property
    def is_development(self) -> bool:
        """Check if running in development environment."""
        return self.environment == "development"

    @property
    def is_production(self) -> bool:
        """Check if running in production environment."""
        return self.environment == "production"

    @property
    def fastapi_kwargs(self) -> dict[str, Any]:
        """Get FastAPI-specific configuration."""
        return {
            "title": self.api_title,
            "description": self.api_description,
            "version": self.api_version,
            "debug": self.debug,
        }

    @property
    def uvicorn_kwargs(self) -> dict[str, Any]:
        """Get Uvicorn-specific configuration."""
        return {
            "host": self.host,
            "port": self.port,
            "reload": self.reload,
            "log_level": self.log_level.lower(),
        }
