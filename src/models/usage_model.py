from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime

from src.shared.declarative_base import Base

# {'resource_type': 'storage', 'tenant': 'tenant-001', 'value': '1536', 'resource_name': 'memory'}
class UsageModel(Base):
    __tablename__ = "usage"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    total_usage = Column(Float, nullable=False)
    total_amount = Column(Float, nullable=False)
    invoice_value = Column(Float, nullable=False)
    paid = Column(Boolean, nullable=False, default=False)
    info = Column(String, nullable=True)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    tenant = relationship(
        "TenantsModel",
        back_populates="usage",
        cascade="all, delete-orphan",
        lazy="joined",
    )
