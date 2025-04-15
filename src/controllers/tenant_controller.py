from src.repositories.tenant_repository import TenantRepository
from src.schema.tenant_schema import TenantSchema
from src.shared.controller_class import Controller
from datetime import datetime


class TenantController(Controller):
    def __init__(self):
        super().__init__()
        self.tenant_repository = TenantRepository()

    async def get_tenant(self, tenant_id: int) -> TenantSchema | None:
        tenant = await self.tenant_repository.find({"id": tenant_id})
        if tenant:
            return TenantSchema.from_orm(tenant)
        return None

    async def create_tenant(self, tenant_data: TenantSchema) -> TenantSchema:
        self.logger.info(f"Creating tenant with data: {tenant_data.dict()}")
        tenant = await self.tenant_repository.insert(tenant_data.dict())
        return TenantSchema.from_orm(tenant)

    async def update_tenant(self, tenant_id: int, tenant_data: TenantSchema) -> TenantSchema:
        self.logger.info(f"Updating tenant with id: {tenant_id} with data: {tenant_data.dict()}")
        tenant = await self.tenant_repository.find({"id": tenant_id})
        if not tenant:
            raise ValueError(f"Tenant with id {tenant_id} not found")
        merge_data = {
            **tenant_data.dict(),
            "tenant_id": tenant.tenant_id,
            "created_at": tenant.created_at,
            "updated_at": datetime.now()
        }
        updated_tenant = await self.tenant_repository.update(tenant_id, merge_data)
        return TenantSchema.from_orm(updated_tenant)
