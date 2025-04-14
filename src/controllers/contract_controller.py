from src.repositories.contract_repository import ContractsRepository
from src.schema.contracts_schema import ContractSchema
from src.shared.controller_class import Controller


class ContractController(Controller):
    def __init__(self):
        super().__init__()
        self.contract_repository = ContractsRepository()

    def create_contract(self, contract_data: ContractSchema):
        return self.contract_repository.insert(**contract_data.dict())
