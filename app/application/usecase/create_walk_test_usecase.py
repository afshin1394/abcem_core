from app.application.cqrs.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.mediator import Mediator
from app.application.usecase.base_use_case import BaseUseCase
from app.domain.cache.cache_gateway import CacheGateway
from app.infrastructure.mapper.mapper import map_models
from app.interfaces.dto.request.walk_test_request import WalkTestRequest


class CreateWalkTestUseCase(BaseUseCase):

    def __init__(self, mediator: Mediator, cache_gateway: CacheGateway):
        self.mediator = mediator
        self.cache_gateway = cache_gateway

    async def execute(self, **kwargs) -> str:
        create_walk_test_request = kwargs.get("create_walk_test_request")
        if isinstance(create_walk_test_request, WalkTestRequest):
            print("walk_test_request" + create_walk_test_request.__str__())
            walk_test_command = await map_models(create_walk_test_request, CreateWalkTestCommand)
            await self.cache_gateway.set(walk_test_command.msisdn, walk_test_command.walk_test_status_id,
                                         3 * 24 * 3600)
            print("walk_test_command" + walk_test_command.__str__())
            await self.mediator.send(walk_test_command)
            return "created"
        else:
            print("The argument is not of type 'create_walk_test_request'")
