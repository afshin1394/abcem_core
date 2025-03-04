from dataclasses import is_dataclass
from typing import Type, TypeVar, List, get_type_hints, Sequence, get_origin, get_args

from pydantic import BaseModel
from sqlalchemy import inspect
from sqlalchemy.orm import ColumnProperty

T = TypeVar("T")
U = TypeVar("U")


async def map_models(source: T, target_class: Type[U]) -> U:
    """
    Maps equivalent properties from the source object to a new instance of target_class
    based on matching attribute names and casts them to the appropriate type in the target class.
    Works with dataclasses, Pydantic models, and SQLAlchemy models.
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
                    target_type = prop.columns[0].type.python_type  # Get the Python type of the column
                    try:
                        # Cast the value to the target type
                        casted_value = target_type(value)
                        init_args[attr] = casted_value
                    except (TypeError, ValueError) as e:
                        # Handle type casting errors (e.g., incompatible types)
                        print(f"Warning: Could not cast {attr} from {type(value)} to {target_type}: {e}")

    # Handle dataclasses
    elif is_dataclass(target_class):
        target_type_hints = get_type_hints(target_class)
        for attr, value in source_attrs.items():
            if attr in target_type_hints:  # Check if the target has the same attribute
                target_type = target_type_hints[attr]
                try:
                    # Cast the value to the target type
                    casted_value = target_type(value)
                    init_args[attr] = casted_value
                except (TypeError, ValueError) as e:
                    # Handle type casting errors (e.g., incompatible types)
                    print(f"Warning: Could not cast {attr} from {type(value)} to {target_type}: {e}")

    # Handle Pydantic models
    elif issubclass(target_class, BaseModel):
        target_fields = target_class.__annotations__
        for attr, value in source_attrs.items():
            if attr in target_fields:  # Check if the target has the same attribute
                target_type = target_fields[attr]
                try:
                    # Cast the value to the target type
                    casted_value = target_type(value)
                    init_args[attr] = casted_value
                except (TypeError, ValueError) as e:
                    # Handle type casting errors (e.g., incompatible types)
                    print(f"Warning: Could not cast {attr} from {type(value)} to {target_type}: {e}")

    else:
        raise TypeError(f"Unsupported target class type: {target_class}")

    # Create an instance of the target class using the collected arguments
    target_instance = target_class(**init_args)
    return target_instance


async def map_models_list(source_list: Sequence[T], target_class: Type[U]) -> List[U]:
    """
    Maps each element of a sequence of source objects (type T) to a new instance
    of target_class (type U), returning a list (Sequence[U]).

    :param source_list: A sequence of source objects to map.
    :param target_class: The class (or possibly a generic like List[SomeClass])
                        to which each source object should be mapped.
    :return: A list (Sequence[U]) of new target_class instances, mapped from the source objects.
    """
    # Safely extract the "real" class if a generic (like List[Customer]) was passed
    origin = get_origin(target_class)
    if origin is not None:
        # If target_class is something like List[Customer]
        # then get_args(target_class) should be (Customer,)
        actual_class = get_args(target_class)[0]
    else:
        # If target_class is already a concrete class like Customer
        actual_class = target_class

    # Use the existing map_models(...) function for each source in source_list
    return [await map_models(source, actual_class) for source in source_list]

