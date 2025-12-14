"""Root API endpoints."""

from fastapi import APIRouter, Request

from agent_template.api.v1.health import HealthResponse, health_check

router = APIRouter()


@router.get("/", response_model=HealthResponse, tags=["health"])
async def health_check_root(request: Request) -> HealthResponse:
    """Health check endpoint at root level."""
    return await health_check(request)
