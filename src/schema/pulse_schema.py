from pydantic import BaseModel

class PulseSchema(BaseModel):
    tenant: str
    product_sku: str
    used_amount: float
    use_unit: str

    class Config:
        orm_mode = True
        from_attributes = True
