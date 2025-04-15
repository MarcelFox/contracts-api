from fastapi import APIRouter

from src.controllers.contract_controller import ContractController
from src.schema.contracts_schema import ContractSchema, ContractResponseSchema

router = APIRouter()

@router.get("/{contract_id}")
async def get_contract(id: int) -> ContractResponseSchema | None:
    return await ContractController().get_contract(id)

@router.post("/")
async def create_contract(contract: ContractSchema) -> ContractResponseSchema:
    return await ContractController().create_contract(contract)


@router.put("/{contract_id}")
async def update_contract(contract_id: int, contract_data: ContractSchema) -> ContractResponseSchema | None:
    return await ContractController().update_contract(contract_id, contract_data)

@router.delete("/{contract_id}")
async def delete_contract(contract_id: int) -> dict:
    return await ContractController().delete_contract(contract_id)
