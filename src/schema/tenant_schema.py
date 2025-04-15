from typing_extensions import Optional
from pydantic import BaseModel
from datetime import datetime
from src.schema.contracts_schema import ContractResponseSchema

class TenantSchema(BaseModel):
    id: Optional[int] = None
    tenant_id: Optional[str] = None
    email: str
    contract_id: Optional[int] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    contract: Optional[ContractResponseSchema] = None

    class Config:
        orm_mode = True
        from_attributes = True
