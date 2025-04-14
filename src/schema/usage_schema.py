from pydantic import BaseModel
from typing import Optional

class UsageSchema(BaseModel):
    total_usage: float
    total_amount: float
    invoice_value: float
    paid: Optional[bool] = None
    info: Optional[str] = None
