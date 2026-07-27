from fastapi import FastAPI
from app.config import settings

from app.api.router import api_router

app = FastAPI(
    title=settings.FASTAPI_SERVICE_NAME,
    version=settings.FASTAPI_VERSION,
)

app.include_router(api_router)