from app.application.cqrs.commands.create_walk_test_command import CreateWalkTestCommand
from app.application.cqrs.shared.command_handler import CommandHandler
from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.repositories.write.write_walk_test_repository import WriteWalkTestRepository
from app.infrastructure.mapper.mapper import map_models


class CreateWalkTestCommandHandler(CommandHandler):
    def __init__(self, write_walk_test_repository: WriteWalkTestRepository):
        self.write_walk_test_repository = write_walk_test_repository

    async def handle(self, command: CreateWalkTestCommand):
        walk_test_domain = await map_models(command, WalkTestDomain)
        print("walk_test_domain" + str(walk_test_domain))
        await self.write_walk_test_repository.create_walk_test(walk_test_domain)


