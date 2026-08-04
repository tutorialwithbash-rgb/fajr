# Docker Compose

This directory contains Docker Compose configurations used to run and manage the platform locally.

## Purpose

Compose defines how platform services are built, connected, and started as a single application stack.

As the platform evolves, additional Compose files may be introduced for development, testing, production, monitoring, or specific platform modules.

## Responsibilities

- Build container images
- Start platform services
- Configure networks
- Mount volumes
- Load environment variables
- Define service dependencies

## Current Services

- FastAPI application
- Nginx gateway

## Usage

Start the platform:

```bash
docker compose -f compose.yml up --build
```

Run in the background:

```bash
docker compose -f compose.yml up --build -d
```

Stop the platform:

```bash
docker compose -f compose.yml down
```