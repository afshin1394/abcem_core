from datetime import time

from app.application.shared.command import Command
from app.domain.enums.complaint_type_enum import ComplaintTypeEnum
from app.domain.enums.problematic_service_enum import ProblematicServiceEnum
from app.domain.enums.technology_enum import TechnologyEnum
from app.domain.enums.walk_test_state_enum import WalkTestStatusEnum


class CreateWalkTestCommand(Command):
    ref_id: str
    province: str
    region: str
    city: str
    is_village: bool
    latitude: float
    longitude: float
    serving_cell: str
    serving_site: str
    is_at_all_hours : bool
    start_time_of_issue: time
    end_time_of_issue: time
    msisdn: str
    technology: TechnologyEnum
    complaint_type: ComplaintTypeEnum
    problematic_service: ProblematicServiceEnum
    related_tt: str
    status: WalkTestStatusEnum





