# FastAPI Image

This directory contains the Docker image definition for the FastAPI application.

## Purpose

The image packages the FastAPI service and its runtime dependencies into a portable container.

## Contents

- `Dockerfile`
- `.dockerignore`
- `entrypoint.sh`

## Build context

This image builds from the FastAPI application source in `applications/FastAPI` and packages it for runtime deployment.

## Build

```bash
docker build \
  -f infrastructure/images/applications/FastAPI/Dockerfile \
  .
```

## Usage

The image is intended to be launched by Docker Compose as part of the platform stack.

The application source remains in `applications/FastAPI`; this directory contains only the container image definition.
