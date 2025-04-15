from typing import Annotated

from fastapi import APIRouter, Depends

from src.controllers.tenant_controller import TenantController
from src.controllers.token_controller import TokenController
from src.schema.tenant_schema import TenantSchema

router = APIRouter()


@router.get("/{tenant_id}")
async def get_tenant(
    tenant_id: int, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> TenantSchema | None:
    return await TenantController().get_tenant(tenant_id)


@router.post("/")
async def create_tenant(
    tenant: TenantSchema, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> TenantSchema:
    return await TenantController().create_tenant(tenant)


@router.put("/{tenant_id}")
async def update_tenant(
    tenant_id: int, tenant_data: TenantSchema, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> TenantSchema | None:
    return await TenantController().update_tenant(tenant_id, tenant_data)


@router.delete("/{tenant_id}")
async def delete_tenant(tenant_id: int, token: Annotated[str, Depends(TokenController().get_current_user)]) -> dict:
    return await TenantController().delete_tenant(tenant_id)
