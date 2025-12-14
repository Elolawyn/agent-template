"""FastAPI application creation and configuration."""

from fastapi import FastAPI

from agent_template.api.root import router as root_router
from agent_template.api.v1.health import router as health_router
from agent_template.config import Settings
from agent_template.lifecycle import lifespan
from agent_template.middleware import setup_middleware


def create_app(settings: Settings) -> FastAPI:
    """Create and configure the FastAPI application.

    Args:
        settings: Validated application settings

    Returns:
        Configured FastAPI application
    """
    app = FastAPI(
        **settings.fastapi_kwargs,
        lifespan=lifespan,
    )

    # Store settings in app state for access in endpoints
    app.state.settings = settings

    # Setup middleware
    setup_middleware(app)

    # Include routers
    app.include_router(root_router)
    app.include_router(health_router, prefix="/api/v1")

    return app
