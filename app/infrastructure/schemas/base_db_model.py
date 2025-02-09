"""Declaring base model classes for sqlalchemy models."""
import uuid

from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import declarative_base, declarative_mixin
from sqlalchemy.sql import func

Base = declarative_base()

class BaseDBModel(Base):
    __abstract__ = True  # <-- Prevent table creation for BaseDBModel
    """Class defining common db model components."""
    # autoinc pk key
    id = Column(String, primary_key=True,default=lambda: str(uuid.uuid4()))
    updated_at = Column(DateTime, server_default=func.now())
    __name__: str

    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    # refresh server defaults with asyncio
    # https://docs.sqlalchemy.org/en/14/orm/extensions/asyncio.html#synopsis-orm
    # required in order to access columns with server defaults
    # or SQL expression defaults, subsequent to a flush, without
    # triggering an expired load
    __mapper_args__ = {"eager_defaults": True}