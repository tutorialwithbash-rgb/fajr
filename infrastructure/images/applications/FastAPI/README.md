# FastAPI Image

This directory contains the Docker image definition for the FastAPI application.

## Purpose

The image packages the FastAPI application and its runtime dependencies into a portable container that can be deployed consistently across environments.

## Contents

- Dockerfile
- .dockerignore
- entrypoint.sh

## Build

```bash
docker build \
    -f infrastructure/images/application/FastAPI/Dockerfile \
    .
```

## Run

The image is intended to be started through Docker Compose.

```
applications/
└── FastAPI/
        ├── README.md
        ├── Dockerfile
        ├── .dockerignore
```

contains the application source code, while this directory contains only the container image definition used to package and run it.