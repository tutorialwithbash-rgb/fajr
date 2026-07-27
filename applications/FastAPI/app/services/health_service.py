from datetime import datetime

from app.schemas.health import HealthResponse
from app.config import settings


def get_health() -> HealthResponse:
    return HealthResponse(
        status="healthy",
        service=settings.FASTAPI_SERVICE_NAME,
        version=settings.FASTAPI_VERSION,
        timestamp=datetime.now()
    )