# Releases

Fajr uses Semantic Versioning for platform releases.

```text
MAJOR.MINOR.PATCH
```

During the development phase, releases remain in the `0.x.x` range.

---

# v0.1.0 — Foundation

**Status:** Released

**Release Type:** Foundation

## Included

- Initial repository architecture
- FastAPI application
- Health check endpoint
- Docker Compose environment
- FastAPI container image
- Nginx container image
- Nginx gateway
- Reverse-proxy foundation
- Module-level documentation
- Central platform documentation
- Architecture diagrams
- Development workflow
- Project roadmap

## Architecture

The release establishes the following basic request path:

```text
Client
   │
   ▼
Nginx Gateway
   │
   ▼
FastAPI Service
```

## Next Release

### v0.2.0 — Networking

Planned capabilities:

- Docker networking
- DNS
- Service discovery
- Internal service communication