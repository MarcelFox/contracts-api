"""Main module."""

from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from src.shared.config import swagger_config
from src.shared.plugins import load_routes_plugin


def create_app() -> FastAPI:
    """App Factory function.

    Returns:
        FastAPI: Server Instance.
    """
    app = FastAPI(**swagger_config)
    load_dotenv()

    class HealthResponse(BaseModel):
        message: str

    @app.get("/")
    async def health_check() -> HealthResponse:
        return HealthResponse(message="ok")

    load_routes_plugin(app)

    return app


app = create_app()
