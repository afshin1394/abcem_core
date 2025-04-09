from app.application.cqrs.shared.query import Query


class GetDeviceInfoByWalkTestIdQuery(Query):
    walk_test_id: str
