import httpx
from fastapi import Depends

from app.domain.services.get_gis_service import GetGISService
from app.domain.services.get_ip_info_service import GetIpInfoService
from app.infrastructure.di.async_client import get_client
from app.infrastructure.repository_impl.get_gis_repository_impl import GetGISServiceImpl
from app.infrastructure.repository_impl.get_ip_info_repository_impl import GetIpInfoServiceImpl



#services
async def get_ip_info_service(client: httpx.AsyncClient = Depends(get_client)) -> GetIpInfoService:
    return GetIpInfoServiceImpl(client=client)


async def get_gis_service() -> GetGISService:
    return GetGISServiceImpl()