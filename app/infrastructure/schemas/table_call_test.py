
from sqlalchemy import Column, Integer, ForeignKey, String

from app.infrastructure.schemas.base_db_model import BaseDBModelWithUUIDPK


class TableCallTest(BaseDBModelWithUUIDPK):
    __tablename__ = 'table_voice_test'
    drop_call = Column(Integer)
    walk_test_detail_id = Column(String,ForeignKey('table_walk_test_detail.id'))
