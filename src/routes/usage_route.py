from fastapi import APIRouter

from src.controllers.usage_controller import UsageController
from src.schema.usage_schema import UsageSchema

router = APIRouter()


@router.post("/")
async def create_usage(usage: UsageSchema) -> UsageSchema | None:
    return await UsageController().create_usage(usage)
