from typing import List

from app.application.mappers.users_mapper import to_domain_list, from_domain
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
        db_result = from_domain(user_domain)
        self.db.add(db_result)
        await self.db.commit()

    async def get_all(self) -> List[UserDomain]:
        # Execute query to fetch all rows from the table
        result = await self.db.execute(select(UsersTable))

        # Extract ORM models (SpeedTestTable instances)
        models = result.scalars().all()

        # Map ORM models to domain models
        return to_domain_list(models)
