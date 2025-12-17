from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from ..core.database import Base

class ClimateHealth(Base):
    __tablename__ = "climate_health_data"

    id = Column(Integer, primary_key=True, index=True)
    province_id = Column(Integer, ForeignKey("provinces.id"), nullable=False)
    date = Column(Date, nullable=False, index=True)
    
    # Climate indicators
    max_temp_c = Column(Float, nullable=True)
    min_temp_c = Column(Float, nullable=True)
    avg_temp_c = Column(Float, nullable=True)
    precipitation_mm = Column(Float, nullable=True)
    relative_humidity_percent = Column(Float, nullable=True)
    
    # Health indicators (example: Malaria)
    malaria_cases = Column(Integer, nullable=True)
    diarrhea_cases = Column(Integer, nullable=True)
    
    # Other potential indicators from the ToR
    renal_diseases_cases = Column(Integer, nullable=True)
    perinatal_health_issues = Column(Integer, nullable=True)
    mental_health_cases = Column(Integer, nullable=True)

    province = relationship("Province")

    __table_args__ = (
        # Unique constraint on date and province
        # to prevent duplicate entries for the same day in the same province
        {"schema": None},
    )
