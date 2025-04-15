from fastapi import APIRouter

from src.controllers.contract_controller import ContractController
from src.schema.contracts_schema import ContractSchema, ContractResponseSchema

router = APIRouter()

@router.get("/{id}")
async def get_contract(id: int) -> ContractResponseSchema | None:
    return await ContractController().get_contract(contract_id=id)

@router.post("/")
async def create_contract(contract: ContractSchema) -> ContractResponseSchema:
    return await ContractController().create_contract(contract)


@router.put("/{id}")
async def update_contract(id: int, contract: ContractSchema) -> ContractResponseSchema | None:
    return await ContractController().update_contract(contract_id=id, contract_data=contract)
