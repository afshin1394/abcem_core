from typing import Sequence, List

from app.domain.entities.speed_test_server_domain import SpeedTestServerDomain
from app.interfaces.dto.response.server_response import SpeedTestServerResponse

def response_to_domain(model: SpeedTestServerResponse) -> SpeedTestServerDomain:
    return SpeedTestServerDomain(
        server_id=model.server_id,
        url=model.url,
        distance=model.distance,
        sponsor=model.sponsor,
        name=model.name,
        country=model.country,
        lat=model.lat,
        lon=model.lon,
        host=model.host,
        cc=model.cc,
    )


def response_list_to_domain_list(models: Sequence[SpeedTestServerResponse]) -> List[SpeedTestServerDomain]:
    return [response_to_domain(model) for model in models]

def response_from_domain(domain: SpeedTestServerDomain) -> SpeedTestServerResponse:
    return SpeedTestServerResponse(
        server_id=domain.server_id,
        url=domain.url,
        distance=domain.distance,
        sponsor=domain.sponsor,
        name=domain.name,
        country=domain.country,
        lat=domain.lat,
        lon=domain.lon,
        host=domain.host,
        cc=domain.cc,
    )

def response_list_from_domain_list(domains: List[SpeedTestServerDomain]) -> List[SpeedTestServerResponse]:
    return [response_from_domain(domain) for domain in domains]