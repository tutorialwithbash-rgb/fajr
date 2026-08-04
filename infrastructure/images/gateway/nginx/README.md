# Nginx Image

This directory contains the Docker image definition for the Nginx gateway.

## Purpose

The image packages the Nginx module into a container for deployment.

## Directory Structure

```text
infrastructure/
└── images/
    └── gateway/
        └── nginx/
            ├── README.md
            ├── Dockerfile
            ├── .dockerignore
```

## Contents

- **Dockerfile** – Builds the Nginx image.
- **.dockerignore** – Excludes unnecessary files from the build context.

## Configuration Source

The runtime configuration is maintained separately in the top-level `nginx/` module. The image packages that configuration and runs Nginx inside a container.

## Build

```bash
docker build \
  -f infrastructure/images/gateway/nginx/Dockerfile \
  .
```

## Usage

This image is intended to be used by Docker Compose and other container orchestration platforms. As the Nginx module evolves, the image packages the latest configuration without requiring changes to the overall image structure.