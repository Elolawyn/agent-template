"""Testing configuration settings for agent template tests."""

from __future__ import annotations

from typing import Any

from pydantic_settings import SettingsConfigDict

from agent_template.config.base import Settings


class TestSettings(Settings):
    """Settings for testing environment."""

    model_config = SettingsConfigDict(
        env_file=".env.test",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="forbid",
    )

    environment: str = "testing"
    host: str = "127.0.0.1"
    port: int = 0  # Use random available port
    debug: bool = True
    reload: bool = False
    log_level: str = "DEBUG"

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
