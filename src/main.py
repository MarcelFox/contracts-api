"""Main module."""
from fastapi import FastAPI
import logging

from dotenv import load_dotenv
from pydantic import BaseModel

from src.models.usage_model import Usage


logger = logging.getLogger("uvicorn")


class HealthResponse(BaseModel):
    message: str = "ok"


def create_app() -> FastAPI:
    """App Factory function.

    Returns:
        FastAPI: Server Instance.
    """
    app = FastAPI()
    load_dotenv()

    # app.add_route(router)

    @app.get("/")
    async def health_check() -> HealthResponse:
        return HealthResponse(message="ok")

    @app.post("/usage")
    async def usage(usage: Usage) -> HealthResponse:
        logger.info(usage)
        return HealthResponse(message="ok")

    return app


app = create_app()
