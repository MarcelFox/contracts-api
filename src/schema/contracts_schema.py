from pydantic import BaseModel

class ContractSchema(BaseModel):
    sku: str
    rate: float
    unit: str
    price: float
