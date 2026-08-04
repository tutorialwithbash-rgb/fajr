# Nginx

This directory contains the Nginx module for the Fajr platform.

## Purpose

Nginx serves as the platform gateway, managing incoming traffic before forwarding requests to services; backend, frontend, database, redis. The module is designed to evolve incrementally as new traffic management capabilities are introduced.

## Responsibilities

Depending on the enabled features, this module may provide:

- Reverse Proxy
- Static Content
- Path Routing
- Load Balancing
- TLS (HTTPS)
- Caching
- Compression
- Security
- Rate Limiting
- AI Gateway

## Directory Structure

```text
nginx/
├── README.md
├── nginx.conf
├── conf.d/
├── snippets/
└── ssl/
```

## Configuration

- **nginx.conf** – Main Nginx configuration.
- **conf.d/** – Server blocks and feature-specific configuration.
- **snippets/** – Reusable configuration fragments.
- **ssl/** – TLS certificates and related configuration.

## Development

This module is developed incrementally. Each feature branch adds or extends Nginx capabilities while preserving the existing configuration.

Examples include:

- `feature/edge-reverse-proxy`
- `feature/edge-static-content`
- `feature/edge-path-routing`
- `feature/edge-load-balancing`
- `feature/edge-tls`
- `feature/edge-caching`
- `feature/edge-compression`
- `feature/edge-security`
- `feature/edge-rate-limiting`
- `feature/edge-ai-gateway`
