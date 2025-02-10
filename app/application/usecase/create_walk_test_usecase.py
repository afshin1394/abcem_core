from typing import Any

from app.application.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.mappers.data_mapper import DataMapper
from app.application.mediator import Mediator
from app.application.usecase.base_use_case import BaseUseCase
from app.interfaces.dto.request.walk_test_request import WalkTestRequest


class CreateWalkTestUseCase(BaseUseCase):
    def __init__(self,mediator: Mediator):
        self.mediator = mediator

    async def execute(self, **kwargs) -> Any:
        create_walk_test_request = kwargs.get("create_walk_test_request")
        if isinstance(create_walk_test_request, WalkTestRequest):
               walk_test_command = DataMapper.dto_to_command(create_walk_test_request,CreateWalkTestCommand)
               await  self.mediator.send(walk_test_command)
        else:
            print("The argument is not of type 'create_walk_test_request'")