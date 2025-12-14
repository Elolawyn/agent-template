"""Main entry point for the Agent Template application."""

import logging
import sys

import uvicorn

from agent_template.app import create_app
from agent_template.config import ConfigurationError, config_manager

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)8s] %(name)s: %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Main function to run the FastAPI application."""
    try:
        # Validate and load configuration before creating the app
        settings = config_manager.validate_and_load()
        logger.info(f"Starting application in {settings.environment} environment")

        # Create FastAPI app with validated settings
        app = create_app(settings)

        # Run the server with uvicorn configuration
        uvicorn.run(
            app,
            **settings.uvicorn_kwargs,
        )

    except ConfigurationError as e:
        logger.error(f"Configuration error: {e.message}")
        sys.exit(1)
    except KeyboardInterrupt:
        logger.info("Application stopped by user")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
