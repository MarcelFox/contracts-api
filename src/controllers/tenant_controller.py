from src.schema.tenant_schema import TenantSchema
from src.shared.controller_class import Controller
from src.repositories.tenant_repository import TenantRepository


class TenantController(Controller):
    def __init__(self):
        super().__init__()
        self.tenant_repository = TenantRepository()

    def create_tenant(self, tenant_data: TenantSchema):
        self.logger.info(f"Creating tenant with data: {tenant_data.dict()}")
        return self.tenant_repository.insert(tenant_data.dict())
