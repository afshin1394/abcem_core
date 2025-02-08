
from pydantic import BaseModel


class UserDomain(BaseModel):
    name : str
    age : int
    gender : str


