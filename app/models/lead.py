from sqlalchemy import Column, Integer, String, DateTime, Text, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import enum

Base = declarative_base()

class TreatmentType(enum.Enum):
    BLOOD_TESTING = "blood_testing"
    PRP = "prp"
    WEIGHT_MANAGEMENT = "weight_management"
    GENERAL_WELLNESS = "general_wellness"

class UrgencyLevel(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"

class Lead(Base):
    __tablename__ = "leads"
    
    id = Column(Integer, primary_key=True, index=True)
    phone_number = Column(String, index=True)
    name = Column(String)
    treatment_type = Column(Enum(TreatmentType))
    urgency_level = Column(Enum(UrgencyLevel))
    health_assessment = Column(Text)
    qualification_score = Column(Integer)  # 1-10 scale
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self):
        return f"<Lead(phone_number='{self.phone_number}', treatment_type='{self.treatment_type}')>"