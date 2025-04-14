from typing_extensions import Optional
from pydantic import BaseModel

class TenantSchema(BaseModel):
    email: str
    contract_id: Optional[int] = None
    usage_id: Optional[int] = None
