import logging
from typing import List

from fastapi import APIRouter, Depends, HTTPException,logger

from app.infrastructure.di.controllers import authentication_controller, get_create_user_controller
from app.interfaces.controllers.authentication_controller import AuthenticationController
from app.interfaces.controllers.user_controller import UserController
from app.interfaces.dto.request.authenticate_request import AuthenticateRequest
from app.interfaces.dto.request.user_create_request import CreateUserRequest
from app.interfaces.dto.response.authenticate_response import AuthenticateResponse
from app.interfaces.dto.response.server_response import SpeedTestServerResponse

# Router for API version 1
router_v1 = APIRouter(
    prefix="/authentication",
)


@router_v1.post("/authenticate", response_model=AuthenticateResponse)
async def login_v1(authenticate_request: AuthenticateRequest,
             authenticate_controller: AuthenticationController = Depends(authentication_controller)):
    try:
        return await authenticate_controller.authenticate(authenticate_request)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router_v1.get("/verify")
async def verify_v1():
    return [{"verify": "true"}]

@router_v1.post("/createUser",response_model=str)
async def create_user_v1(create_user_request : CreateUserRequest,create_user_controller : UserController = Depends(get_create_user_controller)):
    logger.logger.debug(msg= f'create_user_v1 {create_user_request}')
    return await create_user_controller.create_user(create_user_request)

@router_v1.post("/insertSpeed", response_model = List[SpeedTestServerResponse])
async def speed_fetch_v1(user_controller : UserController = Depends(get_create_user_controller)) :
    logger.logger.debug(msg= f'insertSpeed {user_controller}')
    return await user_controller.speed_test_init()