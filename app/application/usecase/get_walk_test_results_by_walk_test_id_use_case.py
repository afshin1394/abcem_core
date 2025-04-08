from app.application.cqrs.queries.get_walk_test_results_by_walk_test_id_query import GetWalkTestResultsByWalkTestIdQuery
from app.application.mediator import Mediator
from app.application.usecase.base_use_case import BaseUseCase
from app.domain.entities.walk_test_results_domain import WalkTestResultsDomain
from app.infrastructure.mapper.mapper import map_models
from app.interfaces.dto.request.walk_test_results_by_walk_test_id_request import WalkTestResultsByWalkTestIdRequest


class GetWalkTestResultsByWalkTestIdUseCase(BaseUseCase):


    def __init__(self,mediator : Mediator) -> None:
        self.mediator = mediator

    async def execute(self, **kwargs) ->  list[WalkTestResultsDomain]:
        walk_test_results_by_walk_test_id_request = kwargs.get("walk_test_results_by_walk_test_id_request")
        if isinstance(walk_test_results_by_walk_test_id_request, WalkTestResultsByWalkTestIdRequest):
            walk_test_results_by_walk_test_id_query = await map_models(walk_test_results_by_walk_test_id_request, GetWalkTestResultsByWalkTestIdQuery)
            return await self.mediator.send(walk_test_results_by_walk_test_id_query)
        else:
            print("The argument is not of type 'WalkTestResultsByWalkTestIdRequest'")
