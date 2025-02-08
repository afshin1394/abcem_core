from fastapi import APIRouter


router_v2 = APIRouter(
    prefix="/validation",
)


@router_v2.get("/validateIp")
def get_ip_info_v2():
    return ["true"]




