from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import create_async_engine

from app.infrastructure.postgres import initialize_database
from app.interfaces.api import router_all
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(app: FastAPI):
    await initialize_database()
    yield


app = FastAPI(docs_url="/api/docs", redoc_url="/api/redoc",lifespan=lifespan)

app.include_router(router_all)
