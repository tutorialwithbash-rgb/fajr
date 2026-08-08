# Docker Compose

This module contains the Docker Compose configuration used to run the Fajr platform locally.

## Purpose

Docker Compose defines how the platform services are built, networked, and started together as a single local stack.

## Responsibilities

- Define platform services and container images
- Configure service networking and dependencies
- Load environment variables and mount volumes
- Provide a local development runtime for the platform

## Current services

- `fastapi` — FastAPI application
- `nginx` — Nginx gateway

## Files

- `compose.yml` — primary Compose file for the current local platform stack

## Usage

This module is referenced by `docs/getting-started.md` for platform startup instructions.

Start the stack locally:

```bash
docker compose -f compose.yml up --build
```

Stop the stack:

```bash
docker compose -f compose.yml down
```

This directory is not intended to contain application internals; it only defines how the platform is assembled and run locally.
