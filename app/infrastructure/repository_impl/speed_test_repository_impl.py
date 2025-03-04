from app.domain.entities.speed_test_server_domain import SpeedTestServerDomain
from app.domain.repositories.speed_test_repository import SpeedTestRepository
from app.infrastructure.mapper.mapper import map_models, map_models_list

from app.infrastructure.schemas.table_speed_test_servers import TableSpeedTestServer
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import List
from sqlalchemy.dialects.postgresql import insert

class SpeedTestRepositoryImpl(SpeedTestRepository):

    def __init__(self, db: AsyncSession):
        self.db = db


    async def save_all(self, results: List[SpeedTestServerDomain]) -> None:
        db_result = await map_models_list(results, TableSpeedTestServer)
        self.db.add_all(db_result)
        await self.db.commit()


    async def get_all(self) -> List[SpeedTestServerDomain]:
        # Execute query to fetch all rows from the table
        result = await self.db.execute(select(TableSpeedTestServer))

        # Extract ORM models (SpeedTestTable instances)
        models = result.scalars().all()

        # Map ORM models to domain models
        return mapp(models,SpeedTestServerDomain)

    async def upsert_servers(self, servers: List[SpeedTestServerDomain]) -> None:
        """
        Perform an upsert operation for the given servers. If a server with the same server_id exists, it will be updated;
        otherwise, it will be inserted.
        """
        # Convert domain models to dictionaries suitable for insertion
        values = [server.model_dump() for server in servers]

        # Create an insert statement with on conflict do update clause
        stmt = insert(TableSpeedTestServer).values(values)
        stmt = stmt.on_conflict_do_update(
            index_elements=["server_id"],  # Unique index to detect conflicts
            set_={
                "sponsor": stmt.excluded.sponsor,
                "name": stmt.excluded.name,
                "country": stmt.excluded.country,
                "lat": stmt.excluded.lat,
                "lon": stmt.excluded.lon,
                "host": stmt.excluded.host,
                "last_updated": stmt.excluded.last_updated,
            },
        )

        # Execute the statement within the session
        await self.db.execute(stmt)
        await self.db.commit()
