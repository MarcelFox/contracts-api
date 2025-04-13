from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.shared.declarative_basemodel import Base
from .contracts_model import ContractsModel


class TenantsModel(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    contract_id = Column(Integer, ForeignKey("usage.id"), nullable=False)

    contract = relationship("ContractsModel", back_populates="tenants")


class TenantSchema(BaseModel):
    id: int
    name: str
    contract_id: int
    contracts: list[ContractsModel] = []
