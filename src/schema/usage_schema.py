from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class UsageSchema(BaseModel):
    id: Optional[int] = None
    total_usage: float
    total_amount: float
    invoice_value: float
    paid: Optional[bool] = None
    info: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True
