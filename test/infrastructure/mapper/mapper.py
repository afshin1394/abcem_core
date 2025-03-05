from dataclasses import dataclass

import pytest
from datetime import  time

from sqlalchemy import Column, Integer

from app.domain.entities.walk_test_domain import WalkTestDomain
from app.domain.enums.complaint_type_enum import ComplaintTypeEnum
from app.domain.enums.problematic_service_enum import ProblematicServiceEnum
from app.domain.enums.service_type_enum import ServiceTypeEnum
from app.domain.enums.technology_enum import TechnologyEnum
from app.domain.enums.walk_test_state_enum import WalkTestStatusEnum
from app.infrastructure.mapper.mapper import map_models
from app.infrastructure.schemas.table_walk_test import TableWalkTest


@dataclass
class A:
   name : str
   datetime : time
@dataclass
class B:
   name : str
   datetime : time
@dataclass
class C:
    name : str
    type : ServiceTypeEnum
@dataclass
class D:
    name = str
    type = Column(Integer)


@pytest.mark.asyncio
async def test_date_mapper():
    a : A = A(name="afshin", datetime=time.fromisoformat("10:18:25"))
    print(await map_models(a,B))

@pytest.mark.asyncio
async def test_time_mapper():
    a : A = A(name="ali", datetime=time.fromisoformat("00:02:334Z"))
    print(await map_models(a,B))
@pytest.mark.asyncio
async def test_enum_mapper():
    c : C = C(name="ali", type=ServiceTypeEnum.FDD)
    print(await map_models(c,D))


@pytest.mark.asyncio
async def test_enum_mapper():
    # Example WalkTestDomain instance
    walk_test_domain = WalkTestDomain(
        ref_id="string",
        province="string",
        region="string",
        city="string",
        is_village=True,
        latitude=0.0,
        longitude=0.0,
        serving_cell="string",
        serving_site="string",
        is_at_all_hours=True,
        start_time_of_issue=time.fromisoformat("13:28:35.463000+00:00"),
        end_time_of_issue=time.fromisoformat("13:28:35.463000+00:00"),
        msisdn="string",
        technology_type_id=TechnologyEnum.NR,  # Enum
        complaint_type_id=ComplaintTypeEnum.POOR_COVERAGE_VOICE,  # Enum
        problematic_service_id=ProblematicServiceEnum.VOICE,  # Enum
        service_type_id=ServiceTypeEnum.FDD,  # Enum
        related_tt="string",
        walk_test_status_id=WalkTestStatusEnum.created  # Enum
    )
    print(await map_models(walk_test_domain,TableWalkTest))