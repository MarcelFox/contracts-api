from sqlalchemy import Column, Integer, String, Float, DateTime, Enum, ForeignKey
from sqlalchemy.orm import relationship
from src.shared.declarative_base import Base
from datetime import datetime

from src.shared.enums import SkuEnum

class ContractsModel(Base):
    __tablename__ = "contracts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    sku = Column(Enum(SkuEnum, name="sku_enum"), nullable=False)
    rate = Column(Float, nullable=False)
    unit = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    effective_date = Column(DateTime, nullable=False)
    usage_id = Column(Integer, ForeignKey("usage.id"), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now())
    updated_at = Column(DateTime, nullable=False, default=datetime.now())

    tenant = relationship(
        "TenantsModel",
        back_populates="contract",
        cascade="all, delete-orphan",
        lazy="joined",
    )

    usage = relationship(
        "UsageModel",
        back_populates="contract",
        lazy="joined",
    )
