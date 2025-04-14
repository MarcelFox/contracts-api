from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from src.shared.declarative_base import Base
import uuid
from datetime import datetime


class TenantsModel(Base):
    __tablename__ = "tenants"

    id = Column(Integer, primary_key=True, index=True)
    tenant_id = Column(
        String, unique=True, nullable=False, default=lambda: uuid.uuid4().hex
    )
    email = Column(String, nullable=False)
    contract_id = Column(Integer, ForeignKey("contracts.id"), nullable=True)
    usage_id = Column(Integer, ForeignKey("usage.id"), nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    contract = relationship(
        "ContractsModel",
        back_populates="tenant",
        lazy="joined",
    )
    usage = relationship(
        "UsageModel",
        back_populates="tenant",
        lazy="joined",
    )
