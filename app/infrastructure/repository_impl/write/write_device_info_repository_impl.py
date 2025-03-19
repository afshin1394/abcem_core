from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.device_info_domain import DeviceInfoDomain
from app.domain.repositories.write.write_device_info_repository import WriteDeviceInfoRepository
from app.infrastructure.schemas.table_device_info import TableDeviceInfo


class WriteDeviceInfoRepositoryImpl(WriteDeviceInfoRepository):

    def __init__(self, db: AsyncSession):
        self.db = db

    async def update_device_info(self, device_info_domain: DeviceInfoDomain):
            # Build the query to find the record by walk_test_id.
            stmt = select(TableDeviceInfo).where(
                TableDeviceInfo.walk_test_id == device_info_domain.walk_test_id
            )
            result = await self.db.execute(stmt)
            existing_device = result.scalar_one_or_none()

            if existing_device:
             existing_device.security_patch = device_info_domain.security_patch
             existing_device.sdk = device_info_domain.sdk
             existing_device.os_version = device_info_domain.os_version
             existing_device.brand = device_info_domain.brand
             existing_device.device = device_info_domain.device
             existing_device.hardware = device_info_domain.hardware
             existing_device.model = device_info_domain.model
             await self.db.commit()
             return "updated"


            else:
             new_device = TableDeviceInfo(
                walk_test_id=device_info_domain.walk_test_id,
                security_patch=device_info_domain.security_patch,
                sdk=device_info_domain.sdk,
                os_version=device_info_domain.os_version,
                brand=device_info_domain.brand,
                device=device_info_domain.device,
                hardware=device_info_domain.hardware,
                model=device_info_domain.model
             )
             self.db.add(new_device)
             await self.db.commit()
             return "created"
