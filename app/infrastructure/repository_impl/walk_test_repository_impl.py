from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.walk_test_repository import WalkTestRepository
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.infrastructure.mapper.mapper import map_models_list, map_models
from app.infrastructure.schemas.table_walk_test import TableWalkTest
from sqlalchemy.future import select


class WalkTestRepositoryImpl(WalkTestRepository):
    def __init__(self, db: AsyncSession):
        self.db = db

    async def save(self, walk_test_domain: WalkTestDomain) -> None:
        result = await map_models(walk_test_domain,TableWalkTest)
        print("walk_test_schema" + str(result))
        self.db.add(result)
        await self.db.commit()

    async def get_all(self) -> List[WalkTestDomain]:
        # Execute query to fetch all rows from the table
        result = await self.db.execute(select(TableWalkTest))

        # Extract ORM models (SpeedTestTable instances)
        models = result.scalars().all()

        # Map ORM models to domain models
        return await map_models_list(models,WalkTestDomain)
