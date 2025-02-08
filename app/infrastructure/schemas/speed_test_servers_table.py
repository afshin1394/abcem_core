import uuid

from sqlalchemy import Column, String, TIMESTAMP, FLOAT
from datetime import datetime

from app.infrastructure.schemas.base_db_model import BaseDBModel, Base


class SpeedTestServerTable(Base, BaseDBModel):
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
    last_updated = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())
