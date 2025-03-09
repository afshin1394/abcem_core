from typing import List

from app.application.cqrs.queries.get_all_technology_types_query import GetAllTechnologyTypesQuery
from app.application.cqrs.shared.query_handler import QueryHandler
from app.domain.entities.technology_type_domain import TechnologyTypeDomain
from app.domain.repositories.read.read_technology_repository import ReadTechnologyRepository


class GetAllTechnologyTypesQueryHandler(QueryHandler[GetAllTechnologyTypesQuery, TechnologyTypeDomain]):

    def __init__(self, read_technology_repository: ReadTechnologyRepository) -> None:
        self.read_technology_repository = read_technology_repository

    async def handle(self, query: GetAllTechnologyTypesQuery) -> List[TechnologyTypeDomain]:
        return await self.read_technology_repository.get_all()


