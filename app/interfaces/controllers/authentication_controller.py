from app.application.commands.authenticate_command import AuthenticateCommand
from app.application.mediator import Mediator
from app.domain.events.authenticated_event import AuthenticatedEvent
from app.interfaces.dto.request.authenticate_request import AuthenticateRequest
from app.interfaces.dto.response.authenticate_response import AuthenticateResponse


class AuthenticationController:
    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    async def authenticate(self, authenticate_request : AuthenticateRequest) -> AuthenticateResponse :
      authenticate_cmd = AuthenticateCommand(msisdn=authenticate_request.msisdn)
      response = await  self.mediator.send(authenticate_cmd)
      # Convert the response to AuthenticateResponse
      if isinstance(response, AuthenticatedEvent):
          return AuthenticateResponse(
             jwt_token= response.jwt_token,
             refresh_token= response.refresh_token
          )
      else:
          raise ValueError("Invalid response type from handler.")
