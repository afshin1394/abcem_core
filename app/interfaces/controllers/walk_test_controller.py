from app.application.usecase.create_walk_test_usecase import CreateWalkTestUseCase
from app.interfaces.dto.request.walk_test_request import WalkTestRequest


class WalkTestController:
    def __init__(self, create_walk_test_use_case: CreateWalkTestUseCase):
            self.create_walk_test_use_case = create_walk_test_use_case
    async  def create_walk_test(self, walk_test_request : WalkTestRequest)->str:
        await self.create_walk_test_use_case.execute(create_user_request= walk_test_request)
        return "created"