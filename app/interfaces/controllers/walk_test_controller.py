from app.application.usecase.create_walk_test_usecase import CreateWalkTestUseCase
from app.application.usecase.get_all_walk_test_by_msisdn_usecase import GetAllWalkTestByMSISDNUseCase
from app.infrastructure.mapper.mapper import map_models_list
from app.interfaces.dto.request.get_walk_test_by_msisdn_request import GetWalkTestByMSISDNRequest
from app.interfaces.dto.request.walk_test_request import WalkTestRequest
from app.interfaces.dto.response.walk_test_by_msisdn_response import WalkTestByMSISDNResponse, WalkTestByMSISDN
from app.interfaces.dto.response.walk_test_created_response import WalkTestCreatedResponse


class WalkTestController:
    def __init__(self, create_walk_test_use_case: CreateWalkTestUseCase,
                 get_all_walk_test_by_msisdn_use_case: GetAllWalkTestByMSISDNUseCase):
        self.create_walk_test_use_case = create_walk_test_use_case
        self.get_all_walk_test_by_msisdn_use_case = get_all_walk_test_by_msisdn_use_case

    async def create_walk_test(self, walk_test_request: WalkTestRequest) -> WalkTestCreatedResponse:
        walk_test_data = await self.create_walk_test_use_case(
            create_walk_test_request=walk_test_request
        )

        # 2. Pass 'walk_test_data' into the model's 'result' field
        response = WalkTestCreatedResponse(status_code = 201,result=walk_test_data)
        print("response" + response.result)
        return response

    async def get_walk_test_by_msisdn(self,
                                      walk_test_by_msisdn_request: GetWalkTestByMSISDNRequest) -> WalkTestByMSISDNResponse:
        walk_test_by_msisdn_domain_list = await self.get_all_walk_test_by_msisdn_use_case.execute(
            get_walk_test_by_msisdn_request=walk_test_by_msisdn_request)
        response_list = await map_models_list(walk_test_by_msisdn_domain_list, WalkTestByMSISDN)
        print("response" + response_list.__str__())
        return WalkTestByMSISDNResponse(result=response_list)
