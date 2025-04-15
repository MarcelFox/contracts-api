from datetime import datetime

from src.repositories.contract_repository import ContractsRepository
from src.repositories.usage_repository import UsageRepository
from src.schema.contracts_schema import ContractResponseSchema, ContractSchema
from src.shared.controller_class import Controller


class ContractController(Controller):
    def __init__(self):
        super().__init__()
        self.contract_repository = ContractsRepository()
        self.usage_repository = UsageRepository()

    async def get_contract(self, contract_id: int) -> ContractResponseSchema | None:
        contract = await self.contract_repository.find(data={"id": contract_id})
        if contract:
            return ContractResponseSchema.from_orm(contract)
        return None

    async def create_contract(self, contract_data: ContractSchema) -> ContractResponseSchema:
        usage = await self.usage_repository.insert({"total_usage": 0, "total_amount": 0, "invoice_value": 0})
        result = await self.contract_repository.insert({**contract_data.dict(), "usage_id": usage.id})
        return ContractResponseSchema.from_orm(result)

    async def update_contract(self, contract_id: int, contract_data: ContractSchema) -> ContractResponseSchema:
        contract = await self.contract_repository.find(data={"id": contract_id})
        if not contract:
            raise ValueError("Contract not found")
        merge_data = {
            **contract_data.__dict__,
            "usage_id": contract.usage_id,
            "created_at": contract.created_at,
            "updated_at": datetime.now(),
        }
        updated_contract = await self.contract_repository.update(id=contract_id, data=merge_data)
        return ContractResponseSchema.from_orm(updated_contract)

    async def delete_contract(self, contract_id: int) -> dict:
        contract = await self.contract_repository.find(data={"id": contract_id})
        if not contract:
            raise ValueError("Contract not found")
        await self.contract_repository.delete(id=contract_id)
        return {"message": f"Contract with id {contract_id} deleted successfully"}
