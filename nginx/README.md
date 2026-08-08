# Nginx Gateway

This module contains the Nginx gateway configuration used by the Fajr platform.

## Purpose

Nginx acts as the platform edge gateway, receiving external HTTP traffic and forwarding it to backend services such as the FastAPI application.

## Responsibilities

- Reverse proxy external requests
- Route requests to backend services
- Host gateway-level configuration
- Provide a foundation for future traffic features such as TLS, caching, and rate limiting

## Current behavior

In the current platform, Nginx forwards requests to the FastAPI service and optionally exposes static or gateway-level routes.

The module does not implement full traffic management yet; it is intended to evolve with the platform.

## Directory layout

```text
nginx/
├── README.md
├── nginx.conf
├── conf.d/
├── snippets/
└── ssl/
```

## Configuration

- `nginx.conf` — main Nginx configuration file.
- `conf.d/` — additional server blocks or route-specific configs.
- `snippets/` — reusable config fragments.
- `ssl/` — TLS certificates and related files.

## Deployment

This module is packaged in the Nginx container image defined at `infrastructure/images/gateway/nginx/Dockerfile` and launched through Docker Compose.

For platform-level startup instructions, see `docs/getting-started.md`.
