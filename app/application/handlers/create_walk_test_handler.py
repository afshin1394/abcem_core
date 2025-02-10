
from app.application.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.mappers.data_mapper import DataMapper
from app.application.shared.command_handler import CommandHandler, C, E
from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.walk_test_repository import WalkTestRepository


class CreateWalkTestHandler(CommandHandler):
    def __init__(self, walk_test_repository: WalkTestRepository):
        self.walk_test_repository = walk_test_repository

    async def handle(self, command: CreateWalkTestCommand) :
        await self.walk_test_repository.save(DataMapper.command_to_domain(command,WalkTestDomain))

    async def deserialize_command(self, json_str: str) -> CreateWalkTestCommand:
        pass