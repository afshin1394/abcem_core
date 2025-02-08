import logging

from app.core.config import settings
from fastapi import logger
from app.infrastructure.schemas.base_db_model import  Base
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio import AsyncEngine, create_async_engine




def get_async_engine() -> AsyncEngine:
    """Return async database engine."""
    try:
        async_engine: AsyncEngine = create_async_engine(
            future=True,
            url=settings.database_url,
        )
        return async_engine
    except SQLAlchemyError as e:
        logger.logger.warning("Unable to establish db engine, database might not exist yet")
        logger.logger.warning(e)



async def initialize_database() -> None:
    """Create table in metadata if they don't exist yet.

    This uses a sync connection because the 'create_all' doesn't
    feature async yet.
    """
    async_engine = get_async_engine()
    async with async_engine.begin() as async_conn:
        await async_conn.run_sync(Base.metadata.create_all)
        logger.logger.log(msg="Initializing database was successful.",level=logging.INFO)









