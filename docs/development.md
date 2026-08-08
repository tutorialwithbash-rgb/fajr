# Development Guide

This document describes the development workflow used by the Fajr project.

---

## Development Philosophy

Fajr follows an incremental engineering approach.

Each platform capability is developed independently, tested locally, documented, and integrated into the main platform.

The goal is to maintain a working system while progressively introducing more advanced infrastructure capabilities.

---

## Branching

The `main` branch represents the current stable state of the platform.

Feature development uses dedicated branches.

Example:

```text
main
│
├── feature/networking
├── feature/container-platform
├── feature/edge-reverse-proxy
├── feature/security
└── feature/observability
```

Use descriptive branch names:

```text
feature/<capability>
```

Examples:

```text
feature/docker-networking
feature/nginx-load-balancing
feature/prometheus-monitoring
```

---

## Commit Convention

Fajr follows the Conventional Commits specification.

Examples:

```text
feat(nginx): add reverse proxy configuration
feat(fastapi): add health endpoint
fix(nginx): correct upstream configuration
docs(root): add central project documentation
refactor(fastapi): simplify health service
test(fastapi): add health endpoint tests
chore(release): prepare v0.1.0
```

### Commit Types

| Type | Purpose |
|---|---|
| `feat` | New functionality |
| `fix` | Bug fix |
| `docs` | Documentation |
| `refactor` | Code restructuring |
| `test` | Tests |
| `chore` | Maintenance |
| `ci` | CI/CD changes |

---

## Development Workflow

```text
Create Branch
     │
     ▼
Implement
     │
     ▼
Test
     │
     ▼
Document
     │
     ▼
Commit
     │
     ▼
Pull Request
     │
     ▼
Review
     │
     ▼
Merge
```

---

## Local Validation

Before merging a change:

1. Verify the application starts.
2. Verify containers build successfully.
3. Verify services communicate correctly.
4. Run available tests.
5. Verify documentation.
6. Review the Git diff.

Useful commands:

```bash
git status
git diff
docker compose config
docker compose ps
docker compose logs
```

---

## Documentation

Every major module should maintain its own README.

Module documentation should describe:

- Purpose
- Responsibilities
- Directory structure
- Configuration
- Usage
- Development workflow

Platform-level concepts belong in `docs/`.

Implementation-specific information belongs with the module.

---

## Releases

Completed milestones are released using Git tags.

Example:

```bash
git tag -a v0.1.0 -m "Release v0.1.0: Foundation"
git push origin v0.1.0
```

See [Releases](releases.md) for the release history.