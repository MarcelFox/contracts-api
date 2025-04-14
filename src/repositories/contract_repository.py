from src.shared.repository_class import Repository
from src.models.contracts_model import ContractsModel
from src.schema.contracts_schema import ContractSchema

class ContractsRepository(Repository[ContractSchema]):
    def __init__(self):
        super().__init__(ContractsModel)
