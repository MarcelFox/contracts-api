from typing import List
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.models.contracts_model import ContractsModel
from src.shared.declarative_basemodel import Base


# {'resource_type': 'storage', 'tenant': 'tenant-001', 'value': '1536', 'resource_name': 'memory'}
class UsageModel(Base):
    __tablename__ = "usage"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    resource_type = Column(String, nullable=False)
    tenant = Column(String, nullable=False)
    value = Column(String, nullable=False)
    resource_name = Column(String, nullable=False)

    contract = relationship("ContractsModel", back_populates="usage")


class Usage(BaseModel):
    resource_type: str
    tenant: str
    value: str
    resource_name: str
    contract: List[ContractsModel] = []
