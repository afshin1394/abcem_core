import json
from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from app.domain.cache.cache_gateway import CacheGateway
from .query import Query  # import your Query base class

Q = TypeVar('Q', bound=Query)  # The specific Query type
R = TypeVar('R')  # The result type (whatever your query returns)


class QueryHandler(ABC, Generic[Q, R]):
    """
    Abstract base class for handling queries and producing results.
    """

    def __init__(self, cache_gateway: CacheGateway, cache_enabled: bool = True, expire: int = 3600):
        self.cache_gateway = cache_gateway
        self.cache_enabled = cache_enabled  # Flag to enable/disable caching
        self.expire = expire

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

    async def execute(self, query) -> dict:
        """Executes the query with optional caching"""
        cache_key = f"query:{query.__class__.__name__}:{json.dumps(query.dict(), sort_keys=True)}"

        # Check cache
        if self.cache_enabled:
            cached_result = await self.cache_gateway.get(cache_key)
            if cached_result:
                return json.loads(cached_result)

        # Execute query
        result = await self.handle(query)

        # Store in cache
        if self.cache_enabled:
            await self.cache_gateway.set(cache_key, json.dumps(result), expiry=self.expire)  # Cache for 5 minutes

        return result
