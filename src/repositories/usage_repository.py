from src.shared.repository_class import Repository
from src.models.usage_model import UsageModel
from src.schema.usage_schema import UsageSchema

class UsageRepository(Repository[UsageSchema]):
    def __init__(self):
        super().__init__(UsageModel)
