# Fajr Documentation

Welcome to the engineering documentation for **Fajr**.

Fajr is an AI Infrastructure Platform designed to demonstrate practical **Platform Engineering, DevOps, Cloud Engineering, and MLOps** through a production-inspired, modular architecture.

This documentation describes the platform architecture, development workflow, roadmap, releases, and operational direction of the project.

---

## Documentation

### Getting Started

- [Getting Started](getting-started.md) — Set up and run Fajr locally.

### Architecture

- [Architecture](architecture.md) — Understand the platform structure, components, and request flow.

### Development

- [Development Guide](development.md) — Development workflow, branching, commits, and contribution practices.

### Platform

- [Roadmap](roadmap.md) — Planned platform capabilities and milestones.
- [Releases](releases.md) — Release history and changes between versions.

---

## Module Documentation

Individual platform modules maintain their own implementation documentation.

| Module | Documentation |
|---|---|
| FastAPI | [FastAPI Service](../applications/FastAPI/README.md) |
| Nginx | [Nginx Gateway](../nginx/README.md) |
| Docker Compose | [Docker Compose](../infrastructure/compose/README.md) |
| FastAPI Image | [FastAPI Image](../infrastructure/images/application/FastAPI/README.md) |
| Nginx Image | [Nginx Image](../infrastructure/images/gateway/nginx/README.md) |

---

## Documentation Structure

```text
docs/
├── README.md
├── getting-started.md
├── architecture.md
├── development.md
├── roadmap.md
├── releases.md
├── diagrams/
│   ├── repository-structure.drawio
│   ├── platform-overview.drawio
│   └── request-flow.drawio
└── assets/
    ├── repository-structure.svg
    ├── platform-overview.svg
    └── request-flow.svg
```

The `diagrams/` directory contains editable Draw.io source files.

The `assets/` directory contains rendered SVG diagrams used by the documentation.

---

## Current Release

**v0.1.0 — Foundation**

The current release establishes the initial application, container, gateway, and documentation foundations for the Fajr platform.