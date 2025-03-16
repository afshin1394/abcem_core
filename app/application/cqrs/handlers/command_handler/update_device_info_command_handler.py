from typing import Optional

from app.application.cqrs.commands.update_device_info_command import UpdateDeviceInfoCommand
from app.application.cqrs.shared.command_handler import CommandHandler, C, E
from app.domain.cache.cache_gateway import CacheGateway
from app.domain.entities.device_info_domain import DeviceInfoDomain
from app.domain.repositories.write.write_device_info_repository import WriteDeviceInfoRepository
from app.infrastructure.mapper.mapper import map_models


class UpdateDeviceInfoCommandHandler(CommandHandler[UpdateDeviceInfoCommand,str]):


    def __init__(self, cache_gateway: CacheGateway , write_device_info_repository : WriteDeviceInfoRepository):
        super().__init__(cache_gateway)
        self.write_device_info_repository = write_device_info_repository

    async def handle(self, command: UpdateDeviceInfoCommand) -> Optional[str]:
       device_info_domain = await map_models(command,DeviceInfoDomain)
       return await self.write_device_info_repository.update_device_info(device_info_domain)
