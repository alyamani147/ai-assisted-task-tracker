# AI-Assisted Task Tracker

A small full-stack Kanban task tracker built through an AI-assisted feature sprint and hardened for the Final Project release.

## Features

1. **Due dates and overdue filter**
   - Optional due date on create and update
   - Overdue state computed by the backend
   - Overdue indicator on task cards
   - API and UI filter for open overdue tasks

2. **Tags and labels**
   - Up to five normalized tags per task
   - Empty tags and tags longer than 24 characters are rejected
   - Tag chips on cards
   - Exact tag filtering in the API and UI

## Technology

- Backend: FastAPI, SQLAlchemy, SQLite
- Frontend: HTML, CSS, vanilla JavaScript
- Tests: pytest and FastAPI TestClient
- Delivery: GitHub Actions and Docker

## Run locally

### Linux, macOS, or WSL

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Windows PowerShell

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`. API documentation is available at `http://127.0.0.1:8000/docs`.

## Run tests

```bash
pytest -v
```

## Final Project

The Final Project extends the fully fixed mid-course application with release-focused deliverables:

- `.github/workflows/ci.yml` runs tests, verifies required artifacts, and builds the Docker image.
- `Dockerfile` packages the FastAPI application and frontend in a non-root container with a health check.
- `.dockerignore` keeps local, generated, sensitive, and assessment-only files out of the build context.
- `AGENTS.md` gives coding agents repository-specific rules and a definition of done.
- `docs/release-evidence.md` records release checks and rollback guidance.
- `docs/final-ai-review.md` documents accepted, edited, and rejected AI output.
- `docs/ai-playbook.md` provides a reusable AI-assisted development workflow.
- The browser application lives in the required `frontend/` directory.

### Run with Docker

```bash
docker build -t ai-assisted-task-tracker .
docker run --rm -p 8000:8000 ai-assisted-task-tracker
```

Then verify:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/api/health
http://127.0.0.1:8000/docs
```

### Final verification

```bash
pytest -v
docker build -t ai-assisted-task-tracker .
git status --short
```

## Project structure

```text
.github/workflows/ci.yml  Continuous integration and Docker build
app/                      FastAPI application, models, schemas, database
frontend/                 Kanban browser interface
tests/                    API tests
docs/                     Final-project evidence, review, and playbook
evidence/                 Mid-course test and break-test records
AGENTS.md                  Repository instructions for coding agents
Dockerfile                 Container image definition
.dockerignore              Docker build-context exclusions
```

## Branch and submission

Start from the fully fixed mid-course branch and create the final branch:

```bash
git checkout mid-course-project
git pull
git checkout -b final-project
git add .
git commit -m "Complete final project release hardening"
git push -u origin final-project
```

Before publishing, verify that no database files, virtual environments, credentials, or generated caches are committed.
