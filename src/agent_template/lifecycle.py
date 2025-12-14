"""Application lifecycle management."""

from contextlib import asynccontextmanager

from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan context manager."""
    # Startup
    print("🚀 Starting Agent Template API...")
    print(f"📋 API Version: {app.version}")
    print(f"🔧 Debug Mode: {app.debug}")
    print("✅ Application started successfully")

    yield

    # Shutdown
    print("🛑 Shutting down Agent Template API...")
    print("🔧 Cleaning up resources...")
    print("✅ Application shutdown complete")
