from app.domain.repositories.read.read_technology_repository import ReadTechnologyRepository
from app.domain.repositories.read.read_walk_test_repository import ReadWalkTestRepository
from app.domain.repositories.speed_test_repository import SpeedTestRepository
from app.domain.repositories.users_repository import UsersRepository
from app.domain.repositories.write.write_walk_test_repository import WriteWalkTestRepository
from app.infrastructure.di.database import get_db
from app.infrastructure.repository_impl.read.read_technology_repository_impl import ReadTechnologyRepositoryImpl
from app.infrastructure.repository_impl.read.read_walk_test_repository_impl import ReadWalkTestRepositoryImpl
from app.infrastructure.repository_impl.speed_test_repository_impl import SpeedTestRepositoryImpl
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from app.infrastructure.repository_impl.users_repository_impl import UsersRepositoryImpl
from app.infrastructure.repository_impl.write.write_walk_test_repository_impl import WriteWalkTestRepositoryImpl


async def get_speed_test_repository(
        async_session: AsyncSession = Depends(get_db),
) -> SpeedTestRepository:
    return SpeedTestRepositoryImpl(db=async_session)


async def get_users_repository(
        async_session: AsyncSession = Depends(get_db),
) -> UsersRepository:
    return UsersRepositoryImpl(db=async_session)


# write repos
async def get_write_walk_test_repository(
        async_session: AsyncSession = Depends(get_db),
) -> WriteWalkTestRepository:
    return WriteWalkTestRepositoryImpl(db=async_session)


# read repos
async def get_read_walk_test_repository(
        async_session: AsyncSession = Depends(get_db),
) -> ReadWalkTestRepository:
    return ReadWalkTestRepositoryImpl(db=async_session)


async def get_technology_type_repository(
        async_session: AsyncSession = Depends(get_db)
) -> ReadTechnologyRepository:
    return ReadTechnologyRepositoryImpl(db=async_session)
