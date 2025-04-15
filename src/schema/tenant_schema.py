from typing_extensions import Optional
from pydantic import BaseModel

class TenantSchema(BaseModel):
    email: str
    contract_id: Optional[int] = None

    class Config:
        orm_mode = True
        from_attributes = True
