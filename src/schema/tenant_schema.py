from typing_extensions import Optional
from pydantic import BaseModel
from datetime import datetime

class TenantSchema(BaseModel):
    id: Optional[int] = None
    tenant_id: Optional[str] = None
    email: str
    contract_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True
