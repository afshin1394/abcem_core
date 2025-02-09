import uuid

from sqlalchemy import Column, String,  BigInteger, TIMESTAMP
from datetime import datetime
from sqlalchemy.sql import func
from app.infrastructure.schemas.base_db_model import BaseDBModel


class UsersTable(BaseDBModel):
    __tablename__ = "users_table"

    name = Column(String)
    age = Column(BigInteger)
    gender = Column(String)
    date_joined = Column(TIMESTAMP, default=func.now(), onupdate=func.now())
