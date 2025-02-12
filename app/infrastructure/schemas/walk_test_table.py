from xmlrpc.client import Boolean
from geoalchemy2 import Geometry
from app.domain.enums.problem_type_enum import ProblemTypeEnum
from app.domain.enums.problematic_service_enum import ProblematicServiceEnum
from app.domain.enums.technology_enum import TechnologyEnum
from sqlalchemy import Column,String,TIMESTAMP,Enum,Boolean,Float
from sqlalchemy.sql import func
from app.domain.enums.walk_test_state_enum import WalkTestStatusEnum
from app.infrastructure.schemas.base_db_model import BaseDBModel


class WalkTestTable(BaseDBModel):
    __tablename__ = "walk_test_table"
    ref_id = Column(String, unique=True)
    province = Column(String, nullable=True)
    region = Column(String, nullable=True)
    city = Column(String, nullable=True)
    is_village = Column(Boolean, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    serving_cell = Column(String, nullable=True)
    serving_site = Column(String, nullable=True)
    problematic_times = Column(String, nullable=True)
    times_of_day = Column(String, nullable=True)
    msisdn = Column(String, nullable=True)
    technology = Column(Enum(TechnologyEnum,name="technology_enum"), nullable=True)
    problem_type = Column(Enum(ProblemTypeEnum,name="problem_type_enum"), nullable=True)
    problematic_service = Column(Enum(ProblematicServiceEnum,name="problematic_service_enum"), nullable=True)
    related_tt = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default=func.now(),nullable=True)
    status = Column(Enum(WalkTestStatusEnum,name="walk_test_status_enum"), nullable=True)
