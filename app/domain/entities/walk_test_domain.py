from dataclasses import dataclass
from datetime import time
from app.domain.enums.complaint_type_enum import ComplaintTypeEnum
from app.domain.enums.problematic_service_enum import ProblematicServiceEnum
from app.domain.enums.technology_enum import TechnologyEnum
from app.domain.enums.walk_test_state_enum import WalkTestStatusEnum


@dataclass
class WalkTestDomain:
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
    problematic_times: str
    msisdn: str
    technology: TechnologyEnum
    complaint_type: ComplaintTypeEnum
    problematic_service: ProblematicServiceEnum
    related_tt: str
    status: WalkTestStatusEnum

    def __repr__(self) -> str:
        return (f"WalkTestDomain(ref_id={self.ref_id}, province={self.province}, region={self.region}, "
                f"city={self.city}, is_village={self.is_village}, latitude={self.latitude}, longitude={self.longitude}, "
                f"serving_cell={self.serving_cell}, serving_site={self.serving_site}, problematic_times={self.problematic_times}, "
                f"times_of_day={self.is_at_all_hours},start_time_of_issue={self.start_time_of_issue},end_time_of_issue={self.end_time_of_issue}, msisdn={self.msisdn}, technology={self.technology.name}, "
                f"complaint_type={self.complaint_type.name}, problematic_service={self.problematic_service.name}, "
                f"related_tt={self.related_tt}, status={self.status.name})")
