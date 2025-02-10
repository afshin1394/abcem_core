
from app.application.mappers.data_mapper import DataMapper
from app.domain.entities.users_domain import UserDomain
from app.domain.repositories.users_repository import UsersRepository
from app.infrastructure.schemas.users_table import UsersTable
from sqlalchemy.ext.asyncio import AsyncSession


from sqlalchemy.future import select
from typing import List

class UsersRepositoryImpl(UsersRepository):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, user_domain: UserDomain) -> None:
        db_result = DataMapper.domain_to_schema(user_domain,UsersTable)
        self.db.add(db_result)
        await self.db.commit()

    async def get_all(self) -> List[UserDomain]:
        # Execute query to fetch all rows from the table
        result = await self.db.execute(select(UsersTable))

        # Extract ORM models (SpeedTestTable instances)
        models = result.scalars().all()

        # Map ORM models to domain models
        return DataMapper.schema_list_to_domain(models,UserDomain)
