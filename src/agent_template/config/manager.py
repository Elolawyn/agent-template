"""Configuration manager for agent template."""

from __future__ import annotations

import logging

from pydantic import ValidationError

from agent_template.config.base import Settings
from agent_template.config.exceptions import ConfigurationError

logger = logging.getLogger(__name__)


class ConfigurationManager:
    """Manages configuration loading and validation."""

    def __init__(self) -> None:
        """Initialize configuration manager."""
        self._settings: Settings | None = None

    def validate_and_load(self, config_file: str | None = None) -> Settings:
        """Validate and load configuration settings.

        Args:
            config_file: Optional path to configuration file

        Returns:
            Validated Settings instance

        Raises:
            ConfigurationError: If validation fails
        """
        try:
            if config_file:
                # Load from file if provided
                from dotenv import load_dotenv

                load_dotenv(config_file)

            # Always validate settings creation
            self._settings = Settings()

            logger.info(
                f"Configuration loaded successfully for environment: {self._settings.environment}"
            )
            return self._settings

        except ValidationError as e:
            self.handle_validation_error(e)
            # This should never be reached due to exception above
            # TODO: Review if this fallback is necessary or can be removed
            # FIXME: Consider refactoring error handling to avoid unreachable code
            raise ConfigurationError(
                "Configuration validation failed"
            ) from e  # pragma: no cover
        except Exception as e:
            error_msg = f"Unexpected error loading configuration: {e}"
            logger.error(error_msg)
            raise ConfigurationError(error_msg) from e

    def handle_validation_error(self, error: ValidationError) -> None:
        """Handle Pydantic validation errors.

        Args:
            error: ValidationError from Pydantic

        Raises:
            ConfigurationError: Always raises with formatted error message
        """
        errors: list[str] = []
        for err in error.errors():
            field_path = " → ".join(str(p) for p in err["loc"])
            msg = err["msg"]
            errors.append(f"  {field_path}: {msg}")

        error_message = (
            "Configuration validation failed:\n"
            + "\n".join(errors)
            + "\n\nPlease check your environment variables and configuration files."
        )

        logger.error(error_message)
        raise ConfigurationError(error_message)

    @property
    def settings(self) -> Settings:
        """Get current settings.

        Returns:
            Current Settings instance

        Raises:
            RuntimeError: If settings not loaded
        """
        if self._settings is None:
            raise RuntimeError("Settings not loaded. Call validate_and_load() first.")
        return self._settings


# Global configuration manager instance
config_manager = ConfigurationManager()
