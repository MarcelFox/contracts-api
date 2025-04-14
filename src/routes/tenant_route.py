from fastapi import APIRouter

from src.controllers.tenant_controller import TenantController
from src.schema.tenant_schema import TenantSchema

router = APIRouter()


@router.post("/")
async def tenant(tenant: TenantSchema) -> TenantSchema | None:
    result = await TenantController().create_tenant(tenant)
    return result
