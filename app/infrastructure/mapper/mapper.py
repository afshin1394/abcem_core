import datetime
from typing import Type, TypeVar, Any, get_origin, Sequence, List, get_args
from sqlalchemy.orm import ColumnProperty
from sqlalchemy import Integer, String, Float, Boolean, inspect
from enum import Enum
from dataclasses import is_dataclass
from pydantic import BaseModel
from typing import get_type_hints

T = TypeVar("T")
U = TypeVar("U")


def cast_value(target_type: Type, value: Any) -> Any:
    """Casts the given value to the target type, with special handling for Enums and SQLAlchemy column types.

    If value is None, returns None without performing any cast.
    """
    if value is None:
        return None

    if target_type == datetime:
        target_type = datetime.datetime

    if isinstance(value, target_type):
        return value

    print("isinstance(value, Enum): " + str(isinstance(value, Enum)))
    if isinstance(value, Enum):
        if isinstance(value.value, int):
            return int(value.value)
        elif isinstance(value.value, str):
            return str(value.value)
        elif isinstance(value.value, float):
            return float(value.value)
        elif isinstance(value.value, bool):
            return bool(value.value)
        else:
            raise ValueError(f"Unsupported Enum value type: {type(value.value)}")

    if isinstance(target_type, type) and issubclass(target_type, Enum):
        try:
            return target_type(value)
        except ValueError:
            raise ValueError(f"Invalid value {value} for Enum {target_type}")

    if target_type == datetime.datetime:
        if isinstance(value, str):
            try:
                return datetime.datetime.fromisoformat(value)
            except Exception as e:
                raise ValueError(f"Error parsing datetime from string {value}: {e}")
        elif isinstance(value, (int, float)):
            try:
                return datetime.datetime.fromtimestamp(value)
            except Exception as e:
                raise ValueError(f"Error converting timestamp {value} to datetime: {e}")

    sqlalchemy_type_mapping = {
        Integer: int,
        String: str,
        Float: float,
        Boolean: bool,
    }

    if target_type in sqlalchemy_type_mapping:
        target_type = sqlalchemy_type_mapping[target_type]

    try:
        return target_type(value)
    except Exception as e:
        raise ValueError(f"Error casting value {value} to {target_type}: {e}")


async def map_models(source: T, target_class: Type[U]) -> U:
    """
    Maps equivalent properties from the source object to a new instance of target_class,
    while handling Enums, SQLAlchemy Column types, Dataclasses, and Pydantic models.
    If the source is a dict, it converts it directly.
    """
    # If the source is a dict, convert directly.
    if isinstance(source, dict):
        if issubclass(target_class, BaseModel):
            # Use Pydantic's validate() (Pydantic v2) or parse_obj() (Pydantic v1)
            return target_class.validate(source)
        else:
            return target_class(**source)

    # Otherwise, extract attributes from the source object.
    source_attrs = vars(source)
    init_args = {}

    # Handle SQLAlchemy models.
    if hasattr(target_class, "__table__"):
        mapper = inspect(target_class)
        for attr, value in source_attrs.items():
            if attr in mapper.attrs:
                prop = mapper.attrs[attr]
                if isinstance(prop, ColumnProperty):
                    column = prop.columns[0]
                    target_type = column.type.python_type
                    casted_value = cast_value(target_type, value)
                    init_args[attr] = casted_value

    # Handle dataclasses.
    elif is_dataclass(target_class):
        target_type_hints = get_type_hints(target_class)
        for attr, value in source_attrs.items():
            if attr in target_type_hints:
                target_type = target_type_hints[attr]
                casted_value = cast_value(target_type, value)
                init_args[attr] = casted_value

    # Handle Pydantic models.
    elif issubclass(target_class, BaseModel):
        target_fields = target_class.__annotations__
        for attr, value in source_attrs.items():
            if attr in target_fields:
                target_type = target_fields[attr]
                casted_value = cast_value(target_type, value)
                init_args[attr] = casted_value

    else:
        raise TypeError(f"Unsupported target class type: {target_class}")

    target_instance = target_class(**init_args)
    return target_instance


async def map_models_list(source_list: Sequence[T], target_class: Type[U]) -> List[U]:
    """
    Maps each element of a sequence of source objects (type T) to a new instance
    of target_class (type U), returning a list.
    """
    origin = get_origin(target_class)
    if origin is not None:
        actual_class = get_args(target_class)[0]
    else:
        actual_class = target_class

    return [await map_models(source, actual_class) for source in source_list]
