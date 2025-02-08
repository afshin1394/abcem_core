from app.domain.repositories.speed_test_repository import SpeedTestRepository
from app.domain.repositories.users_repository import UsersRepository
from app.infrastructure.di.database import get_async_session
from app.infrastructure.repository_impl.speed_test_repository_impl import SpeedTestRepositoryImpl
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.infrastructure.repository_impl.users_repository_impl import UsersRepositoryImpl


async def get_speed_test_repository(
    async_session: AsyncSession = Depends(get_async_session),
) -> SpeedTestRepository:
    return SpeedTestRepositoryImpl(db=async_session)

async def get_users_repository(
        async_session: AsyncSession = Depends(get_async_session),
) -> UsersRepository:
    return  UsersRepositoryImpl(db=async_session)