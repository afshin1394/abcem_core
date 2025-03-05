
from app.application.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.shared.command_handler import CommandHandler
from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.walk_test_repository import WalkTestRepository
from app.infrastructure.mapper.mapper import map_models


class CreateWalkTestCommandHandler(CommandHandler):
    def __init__(self, walk_test_repository: WalkTestRepository):
        self.walk_test_repository = walk_test_repository

    async def handle(self, command: CreateWalkTestCommand) :
        walk_test_domain = await map_models(command,WalkTestDomain)
        print("walk_test_domain"+str(walk_test_domain))
        await self.walk_test_repository.save(walk_test_domain)

    async def deserialize_command(self, json_str: str) -> CreateWalkTestCommand:
        pass