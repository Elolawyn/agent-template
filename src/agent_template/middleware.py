"""Middleware configuration for the FastAPI application."""

import time

from fastapi import FastAPI, Request, Response

# from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint


class TimingMiddleware(BaseHTTPMiddleware):
    """Middleware to add timing information to responses."""

    async def dispatch(
        self, request: Request, call_next: RequestResponseEndpoint
    ) -> Response:
        """Process the request and add timing information."""
        start_time = time.time()
        response = await call_next(request)
        process_time = time.time() - start_time
        response.headers["X-Process-Time"] = str(process_time)
        return response


def setup_middleware(app: FastAPI) -> None:
    """Setup all middleware for the FastAPI application."""

    # CORS middleware
    # app.add_middleware(
    #     CORSMiddleware,
    #     allow_origins=["*"],  # Configure appropriately for production
    #     allow_credentials=True,
    #     allow_methods=["*"],
    #     allow_headers=["*"],
    # )

    # Timing middleware
    # app.add_middleware(TimingMiddleware)

    # Add more middleware here as needed
    # app.add_middleware(OtherMiddleware)
