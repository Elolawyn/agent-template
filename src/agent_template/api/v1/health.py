"""Health check endpoint for API v1."""

from __future__ import annotations

from typing import TYPE_CHECKING

from fastapi import APIRouter, FastAPI, Request

from agent_template.api.models.health_response import HealthResponse

if TYPE_CHECKING:
    from agent_template.config.base import Settings

router = APIRouter(prefix="/health", tags=["health"])


@router.get("/", response_model=HealthResponse)
async def health_check(request: Request) -> HealthResponse:
    """Health check endpoint."""
    app: FastAPI = request.app
    settings: Settings = app.state.settings

    return HealthResponse(
        name=settings.api_title,
        description=settings.api_description,
        version=settings.api_version,
        status="healthy",
    )
