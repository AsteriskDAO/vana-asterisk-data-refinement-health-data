from typing import Optional, List, Dict, Any
from datetime import datetime

from refiner.models.unrefined import HealthData
from refiner.models.refined import HealthDataRefined, Base
from refiner.transformer.base_transformer import DataTransformer

class HealthDataTransformer(DataTransformer):
    def transform(self, data: Dict[str, Any]) -> List[Base]:
        """Transform JSON data into SQLAlchemy model instances."""
        health_data = HealthData(**data)
        refined = HealthDataRefined(
            health_data_id=health_data.healthDataId,
            user_hash=health_data.user_hash,
            research_opt_in=health_data.research_opt_in,
            # Profile fields
            age_range=health_data.profile.age_range if health_data.profile else None,
            ethnicity=health_data.profile.ethnicity if health_data.profile else None,
            location=health_data.profile.location if health_data.profile else None,
            is_pregnant=health_data.profile.is_pregnant if health_data.profile else None,
            # Array fields
            conditions=health_data.conditions,
            medications=health_data.medications,
            treatments=health_data.treatments,
            caretaker=health_data.caretaker,
            timestamp=health_data.timestamp
        )
        return [refined] 