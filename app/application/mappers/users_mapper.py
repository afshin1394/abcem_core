from typing import List, Sequence

from app.domain.entities.users_domain import UserDomain
from app.infrastructure.schemas.users_table import UsersTable


def to_domain(model: UsersTable) -> UserDomain:
    return UserDomain(
        name=model.name,
        age=model.age,
        gender=model.gender,
    )

def to_domain_list(models: Sequence[UsersTable]) -> List[UserDomain]:
    return [to_domain(model) for model in models]

def from_domain(domain: UserDomain) -> UsersTable:
    return UsersTable(
        name=domain.name,
        age=domain.age,
        gender=domain.gender,
    )
def from_domain_list(domains: List[UserDomain]) -> List[UsersTable]:
    return [from_domain(domain) for domain in domains]