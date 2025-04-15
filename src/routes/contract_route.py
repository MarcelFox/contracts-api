from fastapi import APIRouter

from src.controllers.contract_controller import ContractController
from src.schema.contracts_schema import ContractSchema, ContractResponseSchema

router = APIRouter()


@router.post("/")
async def create_contract(contract: ContractSchema) -> ContractResponseSchema:
    return await ContractController().create_contract(contract)
