from typing import List

from app.application.cqrs.queries.get_walk_test_by_msisdn_query import GetWalkTestByMSISDNQuery
from app.application.cqrs.shared.query_handler import QueryHandler
from app.domain.cache.cache_gateway import CacheGateway
from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.read.read_walk_test_repository import ReadWalkTestRepository


class GetWalkTestByMSISDNQueryHandler(QueryHandler[GetWalkTestByMSISDNQuery, WalkTestDomain]):

    def __init__(self, read_walk_test_repository: ReadWalkTestRepository, cache_gateway: CacheGateway,expire : int) -> None:
        super().__init__(cache_gateway,expire=expire)
        self.read_walk_test_repository = read_walk_test_repository

    async def handle(self, query: GetWalkTestByMSISDNQuery) -> List[WalkTestDomain]:
        return await self.read_walk_test_repository.get_all_by_msisdn(query.msisdn)
