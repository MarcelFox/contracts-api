from src.repositories.contract_repository import ContractsRepository
from src.repositories.usage_repository import UsageRepository
from src.schema.contracts_schema import ContractResponseSchema, ContractSchema
from src.shared.controller_class import Controller


class ContractController(Controller):
    def __init__(self):
        super().__init__()
        self.contract_repository = ContractsRepository()
        self.usage_repository = UsageRepository()

    async def create_contract(self, contract_data: ContractSchema) -> ContractResponseSchema:
        usage = await self.usage_repository.insert({"total_usage": 0, "total_amount": 0, "invoice_value": 0})
        result = await self.contract_repository.insert({**contract_data.dict(), "usage_id": usage.id})
        return ContractResponseSchema.from_orm(result)

    async def update_contract(self, contract_id: int, contract_data: ContractSchema) -> ContractResponseSchema:
        contract = await self.contract_repository.find(data={"id": contract_id})
        if not contract:
            raise ValueError("Contract not found")
        updated_contract = await self.contract_repository.update(
            id=contract_id, data={**contract_data.__dict__, **contract.__dict__}
        )
        return ContractResponseSchema.from_orm(updated_contract)
