# FastAPI Service

This module contains the FastAPI application used by the Fajr platform.

## Purpose

The FastAPI service provides the initial application workload for the platform, including an HTTP API and a health endpoint. It is designed to be lightweight and easy to extend as the platform evolves.

## Responsibilities

- Expose application endpoints
- Provide service health and metadata
- Deliver interactive API documentation
- Load configuration from the application module

## Code layout

```text
applications/FastAPI/
├── app/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── health.py
│   │   └── router.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── logging.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── health.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── health_service.py
│   ├── __init__.py
│   ├── config.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_health.py
├── .env
├── README.md
└── requirements.txt
```

## How it works

- `app/main.py` creates the FastAPI application and mounts API routers.
- `app/api/router.py` registers endpoints such as `/health`.
- `app/services/health_service.py` contains the health-check logic.
- `app/schemas/health.py` defines the response model.
- `app/config.py` loads runtime settings and environment values.

## Local development

Install dependencies:

```bash
pip install -r requirements.txt
```

Run locally:

```bash
uvicorn app.main:app --reload
```

This module can also be started through the platform-level Docker Compose stack defined in `infrastructure/compose/compose.yml`.

## Health endpoint

Request:

```http
GET /health
```

The service returns a JSON payload showing service status, version, and timestamp.
