# src/infrastructure/mappers/ip_info_mapper.py
from app.domain.entities.ip_info_domain import IPInfoDomain
from app.infrastructure.remote.dto.ip_info_dto import IpInfoDTO


def map_dto_to_domain(dto: IpInfoDTO) -> IPInfoDomain:
    return IPInfoDomain(
        ip=dto.ip,
        hostname=dto.hostname,
        city=dto.city,
        region=dto.region,
        country=dto.country,
        loc=dto.loc,
        org=dto.org,
        postal=dto.postal,
        timezone=dto.timezone,
        readme=dto.readme,
        state = dto.state
    )

def map_domain_to_dto(domain: IPInfoDomain) -> IpInfoDTO:
    return IpInfoDTO(
        ip=domain.ip,
        hostname=domain.hostname,
        city=domain.city,
        region=domain.region,
        country=domain.country,
        loc=domain.loc,
        org=domain.org,
        postal=domain.postal,
        timezone=domain.timezone,
        readme=domain.readme,
        state=domain.state
    )
