
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, TIMESTAMP, Boolean, Float, ForeignKey, Integer,Time
from sqlalchemy.sql import func
from app.infrastructure.schemas.base_db_model import BaseDBModelWithUUIDPK
from .table_device_info import TableDeviceInfo
from .table_walk_test_detail import TableWalkTestDetail
from .table_technology_type import TableTechnologyType
from .table_complaint_type import TableComplaintType
from .table_problematic_service import TableProblematicService
from .table_walk_test_status import TableWalkTestStatus

class TableWalkTest(BaseDBModelWithUUIDPK):
    __tablename__ = 'table_walk_test'
    ref_id = Column(String, unique=True)
    province = Column(String, nullable=True)
    region = Column(String, nullable=True)
    city = Column(String, nullable=True)
    is_village = Column(Boolean, nullable=True)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    serving_cell = Column(String, nullable=True)
    serving_site = Column(String, nullable=True)
    is_at_all_hours = Column(Boolean, nullable=True)
    start_time_of_issue = Column(Time, nullable=True)
    end_time_of_issue = Column(Time, nullable=True)
    problematic_times = Column(String, nullable=True)
    times_of_day = Column(String, nullable=True)
    msisdn = Column(String, nullable=True)
    related_tt = Column(String, nullable=True)
    created_at = Column(TIMESTAMP, default=func.now(),nullable=True)

    technology_type_id = Column(Integer,ForeignKey('table_technology_type.id'),nullable=True)
    complaint_type_id = Column(Integer,ForeignKey('table_complaint_type.id'),nullable=True)
    problematic_service_id = Column(Integer,ForeignKey('table_problematic_service.id'),nullable=True)
    walk_test_status_id = Column(Integer, ForeignKey('table_walk_test_status.id'),nullable=True)
    device_info_id = Column(String, ForeignKey('table_device_info.id', ondelete="SET NULL"), nullable=True)

    device_info = relationship('TableDeviceInfo',backref='walk_test',uselist=False,single_parent=True,cascade='all, delete-orphan',post_update=True)
    walk_test_details = relationship('TableWalkTestDetail',backref='walk_test',cascade='all, delete-orphan')
    technology_type = relationship('TableTechnologyType')
    complaint_type = relationship('TableComplaintType')
    problematic_service = relationship('TableProblematicService')
    walk_test_status = relationship('TableWalkTestStatus')
