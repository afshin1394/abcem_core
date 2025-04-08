from app.application.cqrs.shared.query import Query


class GetWalkTestResultsByWalkTestIdQuery(Query):
     walk_test_id : str