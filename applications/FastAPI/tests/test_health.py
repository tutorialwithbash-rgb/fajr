from fastapi.testclient import TestClient

from app.config import settings

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")

    assert response.status_code == 200

    body = response.json()

    assert body["status"] == "healthy"
    assert body["service"] == settings.FASTAPI_SERVICE_NAME
    assert body["version"] == settings.FASTAPI_VERSION