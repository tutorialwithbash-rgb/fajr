# Nginx Image

This directory contains the Docker image definition for the Nginx gateway.

## Purpose

The image packages the Nginx gateway configuration and runtime into a container for deployment as part of the Fajr platform.

## Contents

- `Dockerfile`
- `.dockerignore`

## Directory structure

```text
infrastructure/images/gateway/nginx/
├── README.md
├── Dockerfile
└── .dockerignore
```

## Configuration source

The Nginx runtime configuration is maintained in the top-level `nginx/` module. The image only packages that configuration and starts Nginx in a container.

## Build

```bash
docker build \
  -f infrastructure/images/gateway/nginx/Dockerfile \
  .
```

## Usage

This image is intended to be launched via Docker Compose and other orchestration tools. It is not a standalone application repository; it only defines the gateway image build.
