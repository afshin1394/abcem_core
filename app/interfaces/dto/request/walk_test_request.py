
from app.domain.enums.problem_type_enum import ProblemTypeEnum
from app.domain.enums.problematic_service_enum import ProblematicServiceEnum
from app.domain.enums.technology_enum import TechnologyEnum
from app.domain.enums.walk_test_state_enum import WalkTestStatusEnum
from pydantic import BaseModel
from typing import Optional

class WalkTestRequest(BaseModel):
    ref_id: str
    province: Optional[str]
    region: Optional[str]
    city: Optional[str]
    is_village: bool
    latitude: float
    longitude: float
    serving_cell: Optional[str]
    serving_site: Optional[str]
    problematic_times: Optional[str]
    times_of_day: Optional[str]
    msisdn: str
    technology: TechnologyEnum
    problem_type: Optional[ProblemTypeEnum]
    problematic_service: Optional[ProblematicServiceEnum]
    related_tt: Optional[str]
    status: WalkTestStatusEnum
