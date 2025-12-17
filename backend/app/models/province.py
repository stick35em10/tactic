from sqlalchemy import Column, Integer, String, Enum
from ..core.database import Base
import enum

class RegionEnum(str, enum.Enum):
    sul = "Sul"
    centro = "Centro"
    norte = "Norte"

class Province(Base):
    __tablename__ = "provinces"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    region = Column(Enum(RegionEnum), nullable=False)
