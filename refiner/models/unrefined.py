from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime


class Profile(BaseModel):
    age_range: Optional[str]
    ethnicity: Optional[str]
    location: Optional[str]
    is_pregnant: Optional[bool]

class HealthData(BaseModel):
    healthDataId: str
    user_hash: str
    research_opt_in: bool = False
    profile: Optional[Profile]
    conditions: Optional[List[str]] = []
    medications: Optional[List[str]] = []
    treatments: Optional[List[str]] = []
    caretaker: Optional[List[str]] = []
    timestamp: datetime = datetime.now()