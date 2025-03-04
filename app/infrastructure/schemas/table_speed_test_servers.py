
from sqlalchemy import Column, String, TIMESTAMP, FLOAT
from sqlalchemy.sql import func

from app.infrastructure.schemas.base_db_model import BaseDBModelWithUUIDPK


class TableSpeedTestServer(BaseDBModelWithUUIDPK):
    __tablename__ = 'table_speed_test_servers'
    server_id = Column(String, unique=True)
    sponsor = Column(String, nullable=True)
    name = Column(String, nullable=True)
    country = Column(String, nullable=True)
    lat = Column(String, nullable=True)
    lon = Column(String, nullable=True)
    url = Column(String, nullable=True)
    host = Column(String, nullable=True)
    distance = Column(FLOAT, nullable=True)
    cc = Column(String, nullable=True)
    last_updated = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
