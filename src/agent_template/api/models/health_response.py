"""Health check response model for API v1."""

from pydantic import BaseModel


class HealthResponse(BaseModel):
    """Health check response model."""

    name: str
    description: str
    version: str
    status: str
