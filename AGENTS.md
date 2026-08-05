# AGENTS.md

## Project purpose

This repository contains a small full-stack task tracker used to demonstrate a responsible AI-assisted software-development workflow. Preserve the existing FastAPI API, SQLite persistence, vanilla JavaScript frontend, automated tests, CI, and Docker packaging.

## Repository map

- `app/`: FastAPI routes, schemas, models, and database configuration.
- `frontend/`: browser UI served by FastAPI.
- `tests/`: pytest API tests.
- `docs/`: final-project evidence, AI review, and reusable playbook.
- `.github/workflows/ci.yml`: test and Docker-build validation.
- `Dockerfile` and `.dockerignore`: production-style packaging.

## Working rules

1. Read the relevant code and tests before editing.
2. Keep changes scoped and avoid unrelated rewrites.
3. Never commit credentials, tokens, `.env` files, databases, virtual environments, or caches.
4. Add or update tests whenever behavior changes.
5. Run `pytest -v` before considering a change complete.
6. For packaging changes, also run `docker build -t ai-assisted-task-tracker .` when Docker is available.
7. Keep API validation in Pydantic schemas and persistence logic in the application/database layer.
8. Preserve exact-tag filtering and the rule that completed tasks are not overdue.
9. Maintain accessible HTML labels, meaningful button text, and safe text rendering in the frontend.
10. Update README and evidence documents when commands, structure, or behavior change.

## Definition of done

A change is complete only when tests pass, required final-project files remain present, documentation matches the implementation, and no generated or sensitive files are staged.
