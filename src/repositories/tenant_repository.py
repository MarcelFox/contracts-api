from src.shared.repository_class import Repository
from src.models.tenants_model import TenantsModel
from src.schema.tenant_schema import TenantSchema

class TenantRepository(Repository[TenantSchema]):
    def __init__(self):
        super().__init__(TenantsModel)
