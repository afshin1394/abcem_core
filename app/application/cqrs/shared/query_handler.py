# ir/irancell/application/shared/query_handler.py

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from .query import Query  # import your Query base class

Q = TypeVar('Q', bound=Query)  # The specific Query type
R = TypeVar('R')  # The result type (whatever your query returns)


class QueryHandler(ABC, Generic[Q, R]):
    """
    Abstract base class for handling queries and producing results.
    """

    @abstractmethod
    async def handle(self, query: Q) -> R:
        """
        Handle the given query and return the result.

        Args:
            query (Q): The query to handle.

        Returns:
            R: The result of the query.
        """
        pass

