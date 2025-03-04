
from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from app.infrastructure.schemas.base_db_model import BaseDBModelWithUUIDPK
from .table_step_type import TableStepTestType

class TableWalkTestDetail(BaseDBModelWithUUIDPK):
    __tablename__ = 'table_walk_test_detail'
    step_number = Column(Integer)
    step_type_id = Column(Integer,ForeignKey('table_step_test_type.id'))
    walk_test_id = Column(String, ForeignKey('table_walk_test.id'))
    device_info_id = Column(String, ForeignKey('table_device_info.id'))

    step_test_type = relationship('TableStepTestType')
    device_info = relationship('TableDeviceInfo')
