import json

from src.shared.controller_class import Controller
from src.schema.pulse_schema import PulseSchema
from src.repositories.usage_repository import UsageRepository


class PulseController(Controller):
    def __init__(self):
        super().__init__()
        self.usage_repository = UsageRepository()

    async def save_pulse(self, pulse: PulseSchema):
        self.logger.info(f"Pulse -> {json.dumps(pulse.dict(), indent=2)}")
        return await self.usage_repository.insert(
            {
                "total_usage": pulse.used_amount,
                "total_amount": pulse.used_amount,
                "invoice_value": pulse.used_amount,
                "info": "Valor de invoice value é teste",
            }
        )
