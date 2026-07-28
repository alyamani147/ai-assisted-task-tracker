# AI-Assisted Task Tracker

A small full-stack Kanban Task Tracker built with FastAPI, SQLAlchemy, SQLite, and vanilla JavaScript. The project retains the two mid-course features: due dates with overdue filtering, and normalized tags with exact tag filtering.

## Technology
- Backend: FastAPI, SQLAlchemy, SQLite
- Frontend: HTML, CSS, vanilla JavaScript
- Tests: pytest and FastAPI TestClient
- Release checks: GitHub Actions and Docker

## Project structure
```text
.github/workflows/ci.yml  Automated pytest workflow
app/                      API, models, schemas, and database setup
frontend/                 Kanban browser UI
tests/                    API behavior tests
docs/                     Course evidence and ownership documents
Dockerfile                Container build
AGENTS.md                  Repository-specific AI guardrails
```

## Final Project

Branch reviewed: `final-project`

### What this submission demonstrates
- The existing Task Tracker still runs inside the intended course scope.
- CI runs the pytest suite on pushes and pull requests.
- The Docker image builds and runs with `/health` returning HTTP 200.
- AI review, security, verification, and ownership evidence is recorded in `docs/`.
- No new product feature was added during final-project work.

### How to run locally

Linux, macOS, or WSL:
```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Windows PowerShell:
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`. API documentation is at `http://127.0.0.1:8000/docs`, and the release health endpoint is `http://127.0.0.1:8000/health`.

### How to run tests
```bash
python -m pytest -v
```

### How to run with Docker
```bash
docker build -t ai-task-tracker:final .
docker run --rm --name ai-task-tracker -p 8000:8000 ai-task-tracker:final
curl -i http://127.0.0.1:8000/health
```

Expected health response:
```json
{"status":"ok"}
```

Stop the foreground container with `Ctrl+C`. If it was started detached, use:
```bash
docker stop ai-task-tracker
```

### Evidence files
- `docs/release-evidence.md`
- `docs/final-ai-review.md`
- `docs/ai-playbook.md`

### AI assistance summary
AI helped draft and review CI, Docker, repository documentation, and security checks. I verified the result with the full pytest suite, source and diff inspection, local endpoint checks, Docker checks where available, and a manual scan for secrets and unsafe CI shortcuts. I rejected the idea of adding authentication during the final phase because it was a new product feature and explicitly outside the assignment scope.

## Existing product behavior
- Create, update, list, filter, and delete tasks.
- Optional due dates and backend-computed overdue state.
- Completed tasks are not considered overdue.
- Up to five normalized tags per task.
- Exact tag filtering, so `api` does not match `capital`.
- Search, status, priority, tag, and overdue filters can be combined.

## Scope and data note
This is a course project using a local SQLite database. It is not a production service and does not include authentication or multi-user isolation. Only synthetic data should be used.
