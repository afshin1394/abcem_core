
from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship

from app.infrastructure.schemas.base_db_model import BaseDBModelWithUUIDPK


class TableVoiceTest(BaseDBModelWithUUIDPK):
    __tablename__ = 'table_voice_test'
    drop_call = Column(Integer)
    walk_test_id = Column(String,ForeignKey('table_walk_test.id'))
    walk_test = relationship("TableWalkTest")