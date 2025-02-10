from dataclasses import dataclass
from typing import Type, TypeVar, List, Sequence

D = TypeVar("D")  # Generic Type for Domain Models

@dataclass
class BaseDomainModel:

    @classmethod
    def sqlalchemy_to_dataclass(cls, sqlalchemy_instance: T, dataclass_model: Type[D]) -> D:
        """Converts an SQLAlchemy model instance to a domain model (dataclass)."""
        return dataclass_model(**sqlalchemy_instance.__dict__)

    @classmethod
    def sqlalchemy_list_to_dataclass(cls, sqlalchemy_list: Sequence[T], dataclass_model: Type[D]) -> List[D]:
        """Converts a list of SQLAlchemy model instances to domain models (dataclasses)."""
        return [dataclass_model(**item.__dict__) for item in sqlalchemy_list]
