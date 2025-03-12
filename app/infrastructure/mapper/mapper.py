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
    # Do not attempt to cast None values.
    if value is None:
        return None

    # If target_type is datetime module, use datetime.datetime instead.
    if target_type == datetime:
        target_type = datetime.datetime

    # If value is already an instance of target_type, return it directly.
    if isinstance(value, target_type):
        return value

    # Handle Enum -> Corresponding SQLAlchemy Type
    print("isinstance(value, Enum)" + str(isinstance(value, Enum)))
    if isinstance(value, Enum):
        if isinstance(value.value, int):
            return int(value.value)  # Convert Enum(int) -> Integer
        elif isinstance(value.value, str):
            return str(value.value)  # Convert Enum(str) -> String
        elif isinstance(value.value, float):
            return float(value.value)  # Convert Enum(float) -> Float
        elif isinstance(value.value, bool):
            return bool(value.value)  # Convert Enum(bool) -> Boolean
        else:
            raise ValueError(f"Unsupported Enum value type: {type(value.value)}")

    # Handle Primitive Value -> Enum
    if isinstance(target_type, type) and issubclass(target_type, Enum):
        try:
            return target_type(value)  # Convert primitive value to Enum
        except ValueError:
            raise ValueError(f"Invalid value {value} for Enum {target_type}")

    # Special handling for datetime conversion.
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

    # Handle SQLAlchemy Column Type Mapping (Integer, String, Float, Boolean)
    sqlalchemy_type_mapping = {
        Integer: int,
        String: str,
        Float: float,
        Boolean: bool,
    }

    # If the target type is a SQLAlchemy type, map it to Python type.
    if target_type in sqlalchemy_type_mapping:
        target_type = sqlalchemy_type_mapping[target_type]

    # Default: attempt to cast the value to the target type.
    try:
        return target_type(value)
    except Exception as e:
        raise ValueError(f"Error casting value {value} to {target_type}: {e}")


async def map_models(source: T, target_class: Type[U]) -> U:
    """
    Maps equivalent properties from the source object to a new instance of target_class,
    while handling Enums, SQLAlchemy Column types, Dataclasses, and Pydantic models.
    """
    source_attrs = vars(source)  # Get attributes of the source object
    init_args = {}

    # Handle SQLAlchemy models
    if hasattr(target_class, "__table__"):  # Check if it's an SQLAlchemy model
        mapper = inspect(target_class)
        for attr, value in source_attrs.items():
            if attr in mapper.attrs:  # Check if the target has the same attribute
                prop = mapper.attrs[attr]
                if isinstance(prop, ColumnProperty):  # Handle only column properties
                    column = prop.columns[0]
                    target_type = column.type.python_type  # Get Python type

                    # Convert Enums to their corresponding primitive SQLAlchemy type
                    casted_value = cast_value(target_type, value)
                    init_args[attr] = casted_value

    # Handle dataclasses
    elif is_dataclass(target_class):
        target_type_hints = get_type_hints(target_class)
        for attr, value in source_attrs.items():
            if attr in target_type_hints:  # Check if the target has the same attribute
                target_type = target_type_hints[attr]
                casted_value = cast_value(target_type, value)
                init_args[attr] = casted_value

    # Handle Pydantic models
    elif issubclass(target_class, BaseModel):
        target_fields = target_class.__annotations__
        for attr, value in source_attrs.items():
            if attr in target_fields:  # Check if the target has the same attribute
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
    of target_class (type U), returning a list (Sequence[U]).
    """
    # Safely extract the "real" class if a generic (like List[Customer]) was passed.
    origin = get_origin(target_class)
    if origin is not None:
        # If target_class is something like List[Customer],
        # then get_args(target_class) should be (Customer,).
        actual_class = get_args(target_class)[0]
    else:
        # If target_class is already a concrete class like Customer.
        actual_class = target_class

    return [await map_models(source, actual_class) for source in source_list]
