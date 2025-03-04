from app.domain.repositories.speed_test_repository import SpeedTestRepository
from app.domain.repositories.users_repository import UsersRepository
from app.domain.repositories.walk_test_repository import WalkTestRepository
from app.infrastructure.di.database import get_db
from app.infrastructure.repository_impl.speed_test_repository_impl import SpeedTestRepositoryImpl
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.infrastructure.repository_impl.users_repository_impl import UsersRepositoryImpl
from app.infrastructure.repository_impl.walk_test_repository_impl import WalkTestRepositoryImpl


async def get_speed_test_repository(
    async_session: AsyncSession = Depends(get_db),
) -> SpeedTestRepository:
    return SpeedTestRepositoryImpl(db=async_session)

async def get_users_repository(
        async_session: AsyncSession = Depends(get_db),
) -> UsersRepository:
    return  UsersRepositoryImpl(db=async_session)


async def get_walk_test_repository(
        async_session: AsyncSession = Depends(get_db),
)->WalkTestRepository:
    return  WalkTestRepositoryImpl(db=async_session)