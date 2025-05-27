from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base

# Base model for SQLAlchemy
Base = declarative_base()

# Define database models - the schema is generated using these
class HealthDataRefined(Base):
    __tablename__ = 'health_data'
    
    health_data_id = Column(String, primary_key=True)
    user_hash = Column(String, nullable=False)
    research_opt_in = Column(Boolean, default=False)
    # Profile fields embedded directly
    age_range = Column(String)
    ethnicity = Column(String)
    location = Column(String)
    is_pregnant = Column(Boolean)
    # Array fields
    conditions = Column(JSON, default=list)
    medications = Column(JSON, default=list)
    treatments = Column(JSON, default=list)
    caretaker = Column(JSON, default=list)
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)