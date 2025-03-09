from pydantic import BaseModel


class Query(BaseModel):
    """
    Base class for all Queries in the CQRS pattern.
    """

    class Config:
        """
        Configuration for the Command model.

        - allow_population_by_field_name: Allows population of the model using field names instead of aliases.
        - orm_mode: Enables compatibility with ORMs (if needed).
        - arbitrary_types_allowed: Allows arbitrary types (if needed).
        """
        populate_by_name = True
        from_attribute = True
        arbitrary_types_allowed = True
