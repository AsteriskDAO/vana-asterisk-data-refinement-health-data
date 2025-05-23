from datetime import datetime
from sqlalchemy import Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Base model for SQLAlchemy
Base = declarative_base()

# Define database models - the schema is generated using these
class ProfileRefined(Base):
    __tablename__ = 'profiles'
    
    profile_id = Column(Integer, primary_key=True, autoincrement=True)
    age_range = Column(String)
    ethnicity = Column(String)
    location = Column(String)
    is_pregnant = Column(Boolean)
    
    health_data = relationship("HealthDataRefined", back_populates="profile")

class HealthDataRefined(Base):
    __tablename__ = 'health_data'
    
    health_data_id = Column(String, primary_key=True)
    user_hash = Column(String, nullable=False)
    research_opt_in = Column(Boolean, default=False)
    profile_id = Column(Integer, ForeignKey('profiles.profile_id'))
    timestamp = Column(DateTime, nullable=False, default=datetime.utcnow)
    
    profile = relationship("ProfileRefined", back_populates="health_data")
    conditions = relationship("Condition", back_populates="health_data")
    medications = relationship("Medication", back_populates="health_data")
    treatments = relationship("Treatment", back_populates="health_data")
    caretakers = relationship("Caretaker", back_populates="health_data")

class Condition(Base):
    __tablename__ = 'conditions'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    health_data_id = Column(String, ForeignKey('health_data.health_data_id'))
    condition = Column(String, nullable=False)
    
    health_data = relationship("HealthDataRefined", back_populates="conditions")

class Medication(Base):
    __tablename__ = 'medications'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    health_data_id = Column(String, ForeignKey('health_data.health_data_id'))
    medication = Column(String, nullable=False)
    
    health_data = relationship("HealthDataRefined", back_populates="medications")

class Treatment(Base):
    __tablename__ = 'treatments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    health_data_id = Column(String, ForeignKey('health_data.health_data_id'))
    treatment = Column(String, nullable=False)
    
    health_data = relationship("HealthDataRefined", back_populates="treatments")

class Caretaker(Base):
    __tablename__ = 'caretakers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    health_data_id = Column(String, ForeignKey('health_data.health_data_id'))
    caretaker = Column(String, nullable=False)
    
    health_data = relationship("HealthDataRefined", back_populates="caretakers")
