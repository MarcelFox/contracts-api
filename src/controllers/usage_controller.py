from datetime import datetime

from src.repositories.usage_repository import UsageRepository
from src.schema.usage_schema import UsageSchema
from src.shared.controller_class import Controller


class UsageController(Controller):
    def __init__(self):
        super().__init__()
        self.usage_repository = UsageRepository()

    async def get_usage(self, usage_id: int) -> UsageSchema | None:
        usage = await self.usage_repository.find({"id": usage_id})
        if usage:
            return UsageSchema.from_orm(usage)
        return None

    async def create_usage(self, usage_data: UsageSchema) -> UsageSchema:
        self.logger.info(f"Creating usage with data: {usage_data.dict()}")
        usage = await self.usage_repository.insert(usage_data.dict())
        return UsageSchema.from_orm(usage)

    async def update_usage(self, usage_id: int, usage_data: UsageSchema) -> UsageSchema:
        self.logger.info(f"Updating usage with id: {usage_id} with data: {usage_data.dict()}")
        usage = await self.usage_repository.find({"id": usage_id})
        if not usage:
            raise ValueError(f"Usage with id {usage_id} not found")
        updated_usage = await self.usage_repository.update(
            id=usage_id,
            data={
                **usage_data.dict(),
                "paid": usage.paid,
                "created_at": usage.created_at,
                "updated_at": datetime.now(),
            },
        )
        return UsageSchema.from_orm(updated_usage)

    async def delete_usage(self, usage_id: int) -> dict:
        usage = await self.usage_repository.find({"id": usage_id})
        if not usage:
            raise ValueError(f"Usage with id {usage_id} not found")
        await self.usage_repository.delete(usage_id)
        return {"message": f"Usage with id {usage_id} deleted successfully"}
