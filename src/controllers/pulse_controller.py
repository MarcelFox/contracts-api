from src.repositories.tenant_repository import TenantRepository
from src.repositories.usage_repository import UsageRepository
from src.schema.pulse_schema import PulseSchema
from src.schema.usage_schema import UsageSchema
from src.shared.controller_class import Controller


class PulseController(Controller):
    def __init__(self):
        super().__init__()
        self.usage_repository = UsageRepository()
        self.tenant_repository = TenantRepository()

    async def save_pulse(self, pulse: PulseSchema) -> UsageSchema:
        tenant = await self.tenant_repository.find({"tenant_id": pulse.tenant})
        if not tenant:
            raise ValueError(f"Tenant '{pulse.tenant}' not found")

        contract = tenant.__dict__["contract"]
        usage = contract.__dict__["usage"]

        usage.total_usage += pulse.used_amount
        usage.total_amount += pulse.used_amount

        usage.invoice_value = self._calculate_invoice_value(usage, contract)
        result = await self.usage_repository.update(usage.id, UsageSchema.from_orm(usage).dict())
        return UsageSchema.from_orm(result)

    def _calculate_invoice_value(self, usage, contract):
        return usage.total_usage * (contract.price / contract.unit) * contract.rate
