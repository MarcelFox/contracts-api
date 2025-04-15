from typing import Annotated

from fastapi import APIRouter, Depends

from src.controllers.contract_controller import ContractController
from src.controllers.token_controller import TokenController
from src.schema.contracts_schema import ContractResponseSchema, ContractSchema

router = APIRouter()


@router.get("/{contract_id}")
async def get_contract(
    id: int, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> ContractResponseSchema | None:
    return await ContractController().get_contract(id)


@router.post("/")
async def create_contract(
    contract: ContractSchema, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> ContractResponseSchema:
    return await ContractController().create_contract(contract)


@router.put("/{contract_id}")
async def update_contract(
    contract_id: int, contract_data: ContractSchema, token: Annotated[str, Depends(TokenController().get_current_user)]
) -> ContractResponseSchema | None:
    return await ContractController().update_contract(contract_id, contract_data)


@router.delete("/{contract_id}")
async def delete_contract(contract_id: int, token: Annotated[str, Depends(TokenController().get_current_user)]) -> dict:
    return await ContractController().delete_contract(contract_id)
