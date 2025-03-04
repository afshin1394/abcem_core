from contextlib import asynccontextmanager

from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

from app.interfaces.api import router_all
from fastapi import FastAPI

@asynccontextmanager
async def lifespan(app: FastAPI):
    yield

app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc",lifespan=lifespan)



@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=422)

app.include_router(router_all)
