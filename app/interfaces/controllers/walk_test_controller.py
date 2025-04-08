from app.application.usecase.create_walk_test_usecase import CreateWalkTestUseCase
from app.application.usecase.get_all_walk_test_by_msisdn_usecase import GetAllWalkTestByMSISDNUseCase
from app.application.usecase.get_walk_test_results_by_walk_test_id_use_case import GetWalkTestResultsByWalkTestIdUseCase
from app.application.usecase.insert_walk_test_results_use_case import InsertWalkTestResultsUseCase
from app.infrastructure.mapper.mapper import map_models_list
from app.interfaces.dto.request.get_walk_test_by_msisdn_request import GetWalkTestByMSISDNRequest
from app.interfaces.dto.request.walk_test_request import WalkTestRequest
from app.interfaces.dto.request.walk_test_results_by_walk_test_id_request import WalkTestResultsByWalkTestIdRequest
from app.interfaces.dto.request.walk_test_results_request import WalkTestResultsRequest
from app.interfaces.dto.response.walk_test_by_msisdn_response import WalkTestByMSISDNResponse, WalkTestByMSISDN
from app.interfaces.dto.response.walk_test_created_response import WalkTestCreatedResponse
from app.interfaces.dto.response.walk_test_results_by_walk_test_id_response import WalkTestResultsByWalkTestId, \
    WalkTestResultsByWalkTestIdResponse
from app.interfaces.dto.response.walk_test_results_response import WalkTestResultsResponse


class WalkTestController:
    def __init__(self, create_walk_test_use_case: CreateWalkTestUseCase,
                 get_all_walk_test_by_msisdn_use_case: GetAllWalkTestByMSISDNUseCase,
                 insert_walk_test_results_use_case : InsertWalkTestResultsUseCase,
                 get_walk_test_results_by_walk_test_id_use_case: GetWalkTestResultsByWalkTestIdUseCase,
                 ):

        self.create_walk_test_use_case = create_walk_test_use_case
        self.get_all_walk_test_by_msisdn_use_case = get_all_walk_test_by_msisdn_use_case
        self.insert_walk_test_results_use_case = insert_walk_test_results_use_case
        self.get_walk_test_results_by_walk_test_id_use_case = get_walk_test_results_by_walk_test_id_use_case

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


    async def receive_walk_test_results(self,walk_test_results_request : WalkTestResultsRequest) -> WalkTestResultsResponse:
        result = await self.insert_walk_test_results_use_case.execute(walk_test_results_request=walk_test_results_request)
        return WalkTestResultsResponse(status_code = 201,result = result)

    async def get_walk_test_results_by_walk_test_id(self,walk_test_results_bt_walk_test_id_request : WalkTestResultsByWalkTestIdRequest) -> WalkTestResultsByWalkTestIdResponse:
        walk_test_by_walk_test_id_domain_list = await self.get_walk_test_results_by_walk_test_id_use_case.execute(walk_test_results_bt_walk_test_id_request=walk_test_results_bt_walk_test_id_request)
        print("response" + walk_test_by_walk_test_id_domain_list.__str__())
        response_list = await map_models_list(walk_test_by_walk_test_id_domain_list, WalkTestResultsByWalkTestId)

        return WalkTestResultsByWalkTestIdResponse(result = response_list)