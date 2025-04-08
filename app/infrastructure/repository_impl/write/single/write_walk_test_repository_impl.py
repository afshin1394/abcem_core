from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.write.single.write_walk_test_repository import WriteWalkTestRepository
from app.infrastructure.mapper.mapper import map_models
from app.infrastructure.repository_impl.write import BaseWriteDB
from app.infrastructure.schemas.table_walk_test import TableWalkTest


class WriteDBImpl(BaseWriteDB, WriteWalkTestRepository):

    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def create_walk_test(self, walk_test_domain: WalkTestDomain) -> None:
        async with self:
            result = await map_models(walk_test_domain, TableWalkTest)
            self.db.add(result)
