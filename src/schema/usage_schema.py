from pydantic import BaseModel

class UsageSchema(BaseModel):
    resource_type: str
    tenant: str
    value: str
    resource_name: str
