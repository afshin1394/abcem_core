from pydantic import BaseModel
from typing import List, Dict, Optional

from app.interfaces.dto.success_response import BaseSuccessResponse


class SpeedTestServer(BaseModel):
    id: Optional[str]
    sponsor: Optional[str]
    name: Optional[str]
    country: Optional[str]
    lat: Optional[str]
    lon: Optional[str]
    url: Optional[str]
    host: Optional[str]
    d: Optional[float]
    cc: Optional[str]

    class Config:
        json_schema_extra = {
            "example": {
                "url": "http://it3.speedtest.aruba.it:8080/speedtest/upload.php",
                "lat": "45.6983",
                "lon": "9.6773",
                "d": 5343,
                "name": "Ponte San Pietro",
                "country": "Italy",
                "cc": "IT",
                "sponsor": "Aruba S.p.A.",
                "id": "40519",
                "preferred": 0,
                "https_functional": 1,
                "host": "it3.speedtest.aruba.it.prod.hosts.ooklaserver.net:8080",
            }
        }


class SpeedTestServerResponse(BaseSuccessResponse[List[SpeedTestServer]]):
    pass
