
from app.domain.enums.complaint_type_enum import ComplaintTypeEnum
from app.domain.enums.problematic_service_enum import ProblematicServiceEnum
from app.domain.enums.service_type_enum import ServiceTypeEnum
from app.domain.enums.technology_enum import TechnologyEnum
from app.domain.enums.walk_test_state_enum import WalkTestStatusEnum
from pydantic import BaseModel, Field, model_validator
from typing import Optional
from datetime import time

class WalkTestRequest(BaseModel):
    ref_id: Optional[str] = Field(default=None, description="Reference ID for the walk test.")
    province: Optional[str] = Field(default=None, description="Province where the walk test is conducted.")
    region: Optional[str] = Field(default=None, description="Region where the walk test is conducted.")
    city: Optional[str] = Field(default=None, description="City where the walk test is conducted.")
    is_village: Optional[bool] = Field(default=None, description="Indicates if the location is a village.")
    latitude: Optional[float] = Field(default=0.0, description="Latitude of the location.",le= 90 ,ge= -90)
    longitude: Optional[float] = Field(default=0.0, description="Longitude of the location.",le= 180 ,ge= -180)
    serving_cell: Optional[str] = Field(default=None, description="Serving cell information.")
    serving_site: Optional[str] = Field(default=None, description="Serving site information.")
    is_at_all_hours : Optional[bool] = Field(default=None, description="Indicates if the problem is at all hours")
    start_time_of_issue : Optional[time] = Field(default=None, description="Start time of issue.")
    end_time_of_issue : Optional[time] = Field(default=None, description="End time of issue.")
    msisdn: str = Field(default=None, description="MSISDN (phone number) associated with the test.")
    contact_number : str = Field(default=None, description="Contact number.")
    technology_type_id: TechnologyEnum = Field(default=None, description="Technology used in the test.")
    complaint_type_id: Optional[ComplaintTypeEnum] = Field(default=None, description="Type of complaint.")
    problematic_service_id: Optional[ProblematicServiceEnum] = Field(default=None, description="Problematic service.")
    service_type_id : ServiceTypeEnum = Field(default=None, description="Service type.(FDD = 1 or TDD = 2)")
    related_tt: Optional[str] = Field(default=None, description="Related trouble ticket.")
    walk_test_status_id: Optional[WalkTestStatusEnum] = Field(default=None, description="Status of the walk test.")

    @model_validator(mode='after')
    def check_time_order(cls, model: 'WalkTestRequest') -> 'WalkTestRequest':
        if model.start_time_of_issue is not None and model.end_time_of_issue is not None:
            if model.start_time_of_issue >= model.end_time_of_issue:
                raise ValueError("start_time_of_issue must be before end_time_of_issue.")
        return model

    @model_validator(mode='after')
    def check_time_order(cls, model: 'WalkTestRequest') -> 'WalkTestRequest':
        if model.is_at_all_hours is True:
            if model.start_time_of_issue is None or model.end_time_of_issue is None:
                raise ValueError("you must provide start_time_of_issue, end_time_of_issue.")
        return model

    class Config:
        populate_by_name = True
        from_attribute = True
        arbitrary_types_allowed = True


