from dataclasses import dataclass
from typing import List

@dataclass
class SpeedTestServerDomain:
    id: str
    sponsor: str
    name: str
    country: str
    lat: str
    lon: str
    url: str
    host: str
    distance: float
    cc: str

    @staticmethod
    def validate_list(data) -> List:
        """Ensure the data type is a list."""
        return list(data)
