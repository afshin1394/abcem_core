import uuid

from sqlalchemy import Column, String,  BigInteger, TIMESTAMP
from datetime import datetime

from app.infrastructure.schemas.base_db_model import BaseDBModel, Base


class UsersTable(Base,BaseDBModel):
    name = Column(String)
    age = Column(BigInteger)
    gender = Column(String)
    date_joined = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())
