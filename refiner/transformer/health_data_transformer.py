from typing import List, Optional
from datetime import datetime

from refiner.models.unrefined import HealthData, Profile
from refiner.models.refined import (
    ProfileRefined, 
    HealthDataRefined,
    Condition,
    Medication,
    Treatment,
    Caretaker
)

class HealthDataTransformer:
    @staticmethod
    def transform_profile(profile: Optional[Profile]) -> Optional[ProfileRefined]:
        if not profile:
            return None
            
        return ProfileRefined(
            age_range=profile.age_range,
            ethnicity=profile.ethnicity,
            location=profile.location,
            is_pregnant=profile.is_pregnant
        )

    @staticmethod
    def create_conditions(health_data_id: str, conditions: List[str]) -> List[Condition]:
        return [
            Condition(health_data_id=health_data_id, condition=condition)
            for condition in conditions
        ] if conditions else []

    @staticmethod
    def create_medications(health_data_id: str, medications: List[str]) -> List[Medication]:
        return [
            Medication(health_data_id=health_data_id, medication=medication)
            for medication in medications
        ] if medications else []

    @staticmethod
    def create_treatments(health_data_id: str, treatments: List[str]) -> List[Treatment]:
        return [
            Treatment(health_data_id=health_data_id, treatment=treatment)
            for treatment in treatments
        ] if treatments else []

    @staticmethod
    def create_caretakers(health_data_id: str, caretakers: List[str]) -> List[Caretaker]:
        return [
            Caretaker(health_data_id=health_data_id, caretaker=caretaker)
            for caretaker in caretakers
        ] if caretakers else []

    def transform(self, health_data: HealthData) -> tuple[HealthDataRefined, List]:
        # Transform profile first
        profile = self.transform_profile(health_data.profile)
        
        # Create main health data record
        refined_health_data = HealthDataRefined(
            health_data_id=health_data.healthDataId,
            user_hash=health_data.user_hash,
            research_opt_in=health_data.research_opt_in,
            profile=profile,
            timestamp=health_data.timestamp
        )

        # Create related records
        related_records = []
        related_records.extend(self.create_conditions(health_data.healthDataId, health_data.conditions))
        related_records.extend(self.create_medications(health_data.healthDataId, health_data.medications))
        related_records.extend(self.create_treatments(health_data.healthDataId, health_data.treatments))
        related_records.extend(self.create_caretakers(health_data.healthDataId, health_data.caretaker))

        return refined_health_data, related_records 