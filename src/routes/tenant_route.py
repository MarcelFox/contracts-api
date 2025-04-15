from fastapi import APIRouter

from src.controllers.tenant_controller import TenantController
from src.schema.tenant_schema import TenantSchema

router = APIRouter()


@router.get("/{tenant_id}")
async def get_tenant(tenant_id: int) -> TenantSchema | None:
    return await TenantController().get_tenant(tenant_id)


@router.post("/")
async def create_tenant(tenant: TenantSchema) -> TenantSchema:
    return await TenantController().create_tenant(tenant)


@router.put("/{tenant_id}")
async def update_tenant(tenant_id: int, tenant: TenantSchema) -> TenantSchema | None:
    return await TenantController().update_tenant(tenant_id, tenant)
