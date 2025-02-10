from typing import List

from app.application.mappers.data_mapper import DataMapper
from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.walk_test_repository import WalkTestRepository
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.schemas.walk_test_table import WalkTestTable
from sqlalchemy.future import select


class WalkTestRepositoryImpl(WalkTestRepository):
    def __init__(self, db: AsyncSession):
        self.db = db
    async def save(self, walk_test_domain: WalkTestDomain) -> None:
        DataMapper.domain_to_schema(walk_test_domain,WalkTestTable)
        self.db.add(walk_test_domain)
        await self.db.commit()


    async def get_all(self) -> List[WalkTestDomain]:
        # Execute query to fetch all rows from the table
        result = await self.db.execute(select(WalkTestTable))

        # Extract ORM models (SpeedTestTable instances)
        models = result.scalars().all()

        # Map ORM models to domain models
        return DataMapper.schema_list_to_domain(models, WalkTestDomain)
