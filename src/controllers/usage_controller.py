from src.schema.usage_schema import UsageSchema
from src.shared.controller_class import Controller
from src.repositories.usage_repository import UsageRepository


class UsageController(Controller):
    def __init__(self):
        super().__init__()
        self.usage_repository = UsageRepository()

    def create_usage(self, usage_data: UsageSchema):
        self.logger.info(f"Creating usage with data: {usage_data.dict()}")
        return self.usage_repository.insert(usage_data.dict())
