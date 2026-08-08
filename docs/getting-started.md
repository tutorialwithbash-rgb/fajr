# Getting Started

This guide explains how to set up and run the current Fajr platform locally.

---

## Prerequisites

Install the following tools:

- Git
- Docker
- Docker Compose
- Python 3.13+

Verify the installations:

```bash
git --version
docker --version
docker compose version
python --version
```

---

## Clone the Repository

```bash
git clone <repository-url>
cd fajr
```

---

## Run the Platform

The recommended way to run Fajr is through Docker Compose.

```bash
docker compose -f infrastructure/compose/compose.yml up --build
```

To run the platform in the background:

```bash
docker compose -f infrastructure/compose/compose.yml up --build -d
```

---

## Stop the Platform

```bash
docker compose -f infrastructure/compose/compose.yml down
```

---

## Verify the Platform

Once the containers are running, verify the FastAPI health endpoint:

```http
GET /health
```

If the Nginx gateway is exposed on port `80`:

```bash
curl http://localhost/health
```

A successful response should indicate that the service is healthy.

---

## Run FastAPI Directly

The FastAPI service can also be run without Docker.

Navigate to the application:

```bash
cd applications/FastAPI
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Start the development server:

```bash
fastapi dev app/main.py
```

Or with Uvicorn:

```bash
uvicorn app.main:app --reload
```

---

## Interactive API Documentation

FastAPI provides interactive documentation at:

```text
http://localhost/docs
```

and:

```text
http://localhost/redoc
```

---

## Architecture reference

Platform design, request flow, and diagram assets are documented in `docs/architecture.md`.

## Component documentation

- `applications/FastAPI/README.md` — FastAPI application responsibilities and architecture.
- `nginx/README.md` — Nginx gateway configuration and role.
- `infrastructure/compose/README.md` — Docker Compose platform orchestration.
- `infrastructure/images/applications/FastAPI/README.md` — FastAPI container image definition.
- `infrastructure/images/gateway/nginx/README.md` — Nginx container image definition.

---

## Useful Docker Commands

Check running containers:

```bash
docker compose ps
```

View logs:

```bash
docker compose logs
```

View logs for a specific service:

```bash
docker compose logs <service-name>
```

Rebuild the platform:

```bash
docker compose down
docker compose build --no-cache
docker compose up
```

---

## Next Steps

After successfully running Fajr:

1. Read the [Architecture Guide](architecture.md).
2. Read the [Development Guide](development.md).
3. Explore the individual module documentation.
4. Review the [Roadmap](roadmap.md).
5. Review the current [Release](releases.md).
