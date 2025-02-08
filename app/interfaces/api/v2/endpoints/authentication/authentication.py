from fastapi import  APIRouter


router_v2 = APIRouter(
    prefix="/authentication",
)


@router_v2.get("/login")
def login_v2():
    return [{"login": "true"}]

@router_v2.get("/verify")
def verify_v2():
    return [{"verify": "true"}]