from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from pydantic import BaseModel
from src.shared.declarative_basemodel import Base

class ContractsModel(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    tenant_id = Column(Integer, ForeignKey('tenants.id'), nullable=False)
    usage_id = Column(Integer, ForeignKey('usage.id'), nullable=True)
    name = Column(String, nullable=False)

    tenants = relationship("TenantsModel", back_populates="contracts")
    usage = relationship("UsageModel", back_populates="contracts")

class ContractModel(BaseModel):
    id: int
    tenant_id: int
    usage_id: int | None
    name: str
