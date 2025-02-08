

from pydantic import BaseModel
from typing import Optional


class IPInfoDomain(BaseModel):
    ip: Optional[str] = None
    hostname: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    loc: Optional[str] = None
    org: Optional[str] = None
    postal: Optional[str] = None
    timezone: Optional[str] = None
    readme: Optional[str] = None

    class Config:
        from_attribute = True
        json_schema_extra = {
            "example": {
                "ip": "8.8.8.8",
                "hostname": "dns.google",
                "city": "Mountain View",
                "state": "California",
                "region": "North America",
                "country": "US",
                "loc": "37.3861,-122.0839",
                "org": "AS15169 Google LLC",
                "postal": "94043",
                "timezone": "America/Los_Angeles",
                "readme": "https://ipinfo.io/missingauth"
            }
        }

