from typing import  List

from app.application.cqrs.queries.get_all_service_type_query import GetAllServiceTypeQuery
from app.application.mediator import Mediator
from app.application.usecase.base_use_case import BaseUseCase
from app.domain.entities.service_type_domain import ServiceTypeDomain


class GetAllServiceTypeUseCase(BaseUseCase):


    def __init__(self,mediator : Mediator):
        self.mediator = mediator

    async def __execute__(self, **kwargs) -> List[ServiceTypeDomain]:
        return await self.mediator.send(GetAllServiceTypeQuery())
