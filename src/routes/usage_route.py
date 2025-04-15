from typing import Annotated

from fastapi import APIRouter, Depends

from src.controllers.token_controller import TokenController
from src.controllers.usage_controller import UsageController
from src.schema.usage_schema import UsageSchema

router = APIRouter()


@router.get("/{usage_id}")
async def get_usage(
    usage_id: int, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> UsageSchema | None:
    return await UsageController().get_usage(usage_id)


@router.post("/")
async def create_usage(
    usage: UsageSchema, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> UsageSchema:
    return await UsageController().create_usage(usage)


@router.put("/{usage_id}")
async def update_usage(
    usage_id: int, usage_data: UsageSchema, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> UsageSchema:
    return await UsageController().update_usage(usage_id, usage_data)


@router.delete("/{usage_id}")
async def delete_usage(usage_id: int, token: Annotated[str, Depends(TokenController().get_current_user)]) -> dict:
    return await UsageController().delete_usage(usage_id)
