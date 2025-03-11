import json
import time
from contextlib import asynccontextmanager
from typing import cast

from starlette.responses import  Response

from app.interfaces.api import router_all
from fastapi import FastAPI, HTTPException, Request

from fastapi.exceptions import RequestValidationError

from app.interfaces.dto.error_response import ErrorResponse
from app.interfaces.dto.success_response import BaseSuccessResponse
from app.interfaces.open_api import custom_openapi


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc", lifespan=lifespan)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return ErrorResponse(
        status_code=exc.status_code,
        content={
            "message": exc.detail if isinstance(exc.detail, str) else "HTTP Error occurred",
            "code": exc.status_code,
            "errors": [str(exc.detail)] if isinstance(exc.detail, str) else []
        },
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    # Format the list of errors as needed
    errors = [f"{'.'.join(map(str, err['loc']))}: {err['msg']}" for err in exc.errors()]
    return ErrorResponse(
        status_code=422,
        content={
            "message": "Validation error",
            "code": 422,
            "errors": errors
        },
    )


@app.exception_handler(Exception)
async def general_exception_handler(request: Request, exc: Exception):
    # Optional: Log the exception details here
    return ErrorResponse(
        status_code=500,
        content={
            "message": "An unexpected error occurred",
            "code": 500,
            "errors": [str(exc)]
        },
    )
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()  # Use perf_counter for high resolution
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    response.headers["X-Process-Time"] = f"{process_time:.4f}"
    print("isinstance(response, BaseSuccessResponse)"+isinstance(response, BaseSuccessResponse).__str__())

    if isinstance(response, BaseSuccessResponse):
        success_response = cast(BaseSuccessResponse, response)
        success_response.latency = process_time
        return success_response

    return response

app.include_router(router_all)
app.openapi_schema = custom_openapi(app=app)
