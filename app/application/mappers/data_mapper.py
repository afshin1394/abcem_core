from typing import Type, TypeVar, List, Sequence
from sqlalchemy.orm import DeclarativeBase
from pydantic import BaseModel

T = TypeVar("T", bound=DeclarativeBase)
D = TypeVar("D")  # Generic Type for Domain Models
P = TypeVar("P")  # Generic Type for DTO Models
C = TypeVar("C")  # Generic Type for Commands

class DataMapper:
    @classmethod
    def domain_to_schema(cls, dataclass_instance: object, sqlalchemy_model: Type[T]) -> T:
        """Converts a domain model (dataclass) instance to an SQLAlchemy model."""
        return sqlalchemy_model(**dataclass_instance.__dict__)

    @classmethod
    def domain_list_to_schema(cls, dataclass_list: Sequence[object], sqlalchemy_model: Type[T]) -> List[T]:
        """Converts a list of domain model (dataclass) instances to SQLAlchemy models."""
        return [sqlalchemy_model(**item.__dict__) for item in dataclass_list]

    @classmethod
    def schema_to_domain(cls, sqlalchemy_instance: T, dataclass_model: Type[D]) -> D:
        """Converts an SQLAlchemy model instance to a domain model (dataclass)."""
        return dataclass_model(**sqlalchemy_instance.__dict__)

    @classmethod
    def schema_list_to_domain(cls, sqlalchemy_list: Sequence[T], dataclass_model: Type[D]) -> List[D]:
        """Converts a list of SQLAlchemy model instances to domain models (dataclasses)."""
        return [dataclass_model(**item.__dict__) for item in sqlalchemy_list]

    @classmethod
    def dto_list_to_domain(cls, pydantic_list: Sequence[P], domain_model: Type[D]) -> List[D]:
        return [domain_model(**item.dict()) for item in pydantic_list]

    @classmethod
    def domain_list_to_dto(cls, dataclass_list: Sequence[D], pydantic_model: Type[P]) -> List[P]:
        return [pydantic_model(**item.__dict__) for item in dataclass_list]

    @classmethod
    def dto_to_domain(cls, pydantic_instance: P, domain_model: Type[D]) -> D:
        return domain_model(**pydantic_instance.dict())

    @classmethod
    def domain_to_dto(cls, dataclass_instance: D, pydantic_model: Type[P]) -> P:
        return pydantic_model(**dataclass_instance.__dict__)

    @classmethod
    def command_to_domain(cls,command_instance: BaseModel, domain_model: Type[D]) -> D:
        command_dict = {key: value for key, value in command_instance.__dict__.items() if key != 'correlation_id'}
        return domain_model(**command_dict)

    @classmethod
    def query_to_domain(cls,query_instance: BaseModel, domain_model: Type[D]) -> D:
        return domain_model(**query_instance.__dict__)

    @classmethod
    def dto_to_command(cls,dto_instance: BaseModel, command_model: Type[C]) -> C:
        return command_model(**dto_instance.__dict__)
