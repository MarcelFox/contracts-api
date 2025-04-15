from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from src.schema.usage_schema import UsageSchema
from src.shared.enums import SkuEnum


class ContractSchema(BaseModel):
    id: Optional[int] = None
    sku: SkuEnum
    rate: float
    unit: str
    price: float
    usage_id: Optional[int] = None
    effective_date: datetime
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True


class ContractResponseSchema(BaseModel):
    id: int
    sku: SkuEnum
    rate: float
    unit: str
    price: float
    effective_date: datetime
    usage: UsageSchema
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True
