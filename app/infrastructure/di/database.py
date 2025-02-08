"""Database ependancies for FastApi app.


"""
from typing import AsyncGenerator

from fastapi import logger
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

from app.infrastructure.postgres import get_async_engine


# DB dependency
async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    """Yield an async session.

    All conversations with the database are established via the session
    objects. Also. the sessions act as holding zone for ORM-mapped objects.
    """
    async_session  = sessionmaker(
        bind=get_async_engine(),
        expire_on_commit=False,
        class_=AsyncSession,
        autoflush=False,
        autocommit=False,
    )

    async with async_session() as async_sess:
        try:
            yield async_sess

        except SQLAlchemyError as e:
            logger.logger.error("Unable to yield session in database dependency")
            logger.logger.error(e)
