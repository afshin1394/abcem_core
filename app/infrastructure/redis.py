# infrastructure/cache/redis_client.py
from typing import Optional

from redis.asyncio import Redis

from app.core.config import settings


class RedisClient:
    _instance: Optional['RedisClient'] = None

    def __init__(self, redis_url: str):
        self.redis_url = redis_url
        self.redis = None

    @classmethod
    async def get_instance(cls, redis_url: str = f'{settings.redis_url}') -> 'RedisClient':
        if cls._instance is None:
            cls._instance = RedisClient(redis_url)
            cls._instance.redis = await Redis.from_url(redis_url, decode_responses=True)
        return cls._instance

    async def invalidate_keys(self, keys: list):
        if not keys:
            return
        await self.redis.delete(*keys)

    async def get(self, key: str):
        return await self.redis.get(key)

    async def set(self, key: str, value, expire: int = 3600):
        await self.redis.set(key, value, ex=expire)
