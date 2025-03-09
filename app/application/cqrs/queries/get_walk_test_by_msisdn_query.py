from app.application.cqrs.shared.query import Query


class GetWalkTestByMSISDNQuery(Query):
    msisdn: str
