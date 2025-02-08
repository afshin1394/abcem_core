from app.application.commands.authenticate_command import AuthenticateCommand
from app.application.shared.command_handler import CommandHandler, C
from app.domain.events.authenticated_event import AuthenticatedEvent
from app.domain.services.get_ip_info_service import GetIpInfoService


def generate_refresh_token(msisdn: str) -> str:
     # Placeholder for refresh token generation
     # Replace this with actual refresh token logic
    return f"refresh_token_for_{msisdn}"


def generate_jwt_token(msisdn: str) -> str:
    # Placeholder for JWT token generation
    # Replace this with actual JWT logic
    return f"jwt_token_for_{msisdn}"


class AuthenticateCommandHandler(CommandHandler):

    async def deserialize_command(self, json_str: str) -> C:
        pass

    def __init__(self, isp_service: GetIpInfoService):
        self.isp_service = isp_service

    async def handle(self, command: AuthenticateCommand) -> AuthenticatedEvent:
        isp = await self.isp_service.get_ip_info()
        valid = isp.hostname.__contains__("Irancell")

        if not valid:
            raise ValueError(f"Login from ISP '{isp}' is not allowed.")
        else:
            return AuthenticatedEvent(
                is_ip_valid= valid,
                jwt_token = generate_jwt_token(command.msisdn),
                refresh_token = generate_refresh_token(command.msisdn)
            )

        # Proceed with authentication logic
        # Example: Verify username and password

        # Generate and return a session token or user data

