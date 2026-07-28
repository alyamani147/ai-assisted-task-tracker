# AGENTS.md

## Purpose
This repository is a course Task Tracker release. Preserve existing behavior and scope. Do not add product features during final-project work.

## Read first
Before editing, read `README.md`, `docs/release-evidence.md`, `docs/final-ai-review.md`, and the relevant tests. Inspect the current diff before proposing changes.

## Stack
- Python 3.13
- FastAPI and Uvicorn
- SQLAlchemy with local SQLite
- Pydantic
- Vanilla HTML, CSS, and JavaScript in `frontend/`
- pytest and FastAPI TestClient

## Commands
```bash
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
python -m pytest -v
docker build -t ai-task-tracker:final .
docker run --rm -p 8000:8000 ai-task-tracker:final
curl -i http://127.0.0.1:8000/health
```

## Project rules
1. Do not add authentication, comments, notifications, a production database, or unrelated UI changes.
2. Treat `app/` and `frontend/` as protected. Change them only for a small verified bug fix, security fix, or documentation-supported correction.
3. Any change to `app/` or `frontend/` must be explained in `docs/final-ai-review.md` and covered by tests or a manual check.
4. Do not weaken tests, skip pytest, add `continue-on-error`, use `|| true`, or hide failing commands.
5. Keep `/health` returning HTTP 200 with `{"status":"ok"}`.
6. Preserve exact tag filtering and the rule that completed tasks are not overdue.

## Data and security guardrails
- Never paste or commit real credentials, tokens, `.env` values, production logs, customer data, or personal data.
- Do not copy `.env`, database files, caches, or logs into the Docker image.
- Use only synthetic task data in tests and documentation.
- Prefer read-only review commands before making edits.

## Review and verification
- Explain every changed line and configuration choice.
- Inspect `git diff --check` and `git diff` before committing.
- Run `python -m pytest -v` after code or dependency changes.
- Build and run Docker after Dockerfile or runtime-command changes.
- Grade AI review findings as useful, noise, wrong, valid, or false positive; do not accept them blindly.
