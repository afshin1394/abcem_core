from typing import List

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.read.read_walk_test_repository import ReadWalkTestRepository
from app.infrastructure.mapper.mapper import map_models_list
from app.infrastructure.schemas.table_walk_test import TableWalkTest


class ReadWalkTestRepositoryImpl(ReadWalkTestRepository):

    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    async def get_all_by_msisdn(self, msisdn: str) -> List[WalkTestDomain]:
        result = await self.db.execute(
            select(TableWalkTest).where(TableWalkTest.msisdn == msisdn).order_by(TableWalkTest.created_at.asc())
        )
        records = result.scalars().all()
        print(f"records {records.__str__()}")
        list_of_walk_test_domain = await map_models_list(records, WalkTestDomain)
        print(f"list_of_walk_test_domain {list_of_walk_test_domain.__str__()}")
        return list_of_walk_test_domain
