# AI-Assisted Task Tracker

A small full-stack Kanban task tracker built for the Mid-Course AI-Assisted Feature Extension Sprint.

## Selected features

1. **Due dates and overdue filter**
   - Optional due date on create and update
   - Overdue state computed by the backend
   - Overdue pill on task cards
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

## Run the backend and frontend

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

Open `http://127.0.0.1:8000` in a browser. The API documentation is available at `http://127.0.0.1:8000/docs`.

## Run tests

```bash
pytest -v
```

## Project structure

```text
app/                 FastAPI application, models, schemas, database
static/              Kanban frontend
tests/               API tests
docs/midcourse/      Required project evidence and reflection
```

## Branch and submission

Create and submit the branch required by the brief:

```bash
git checkout -b mid-course-project
git add .
git commit -m "Complete mid-course task tracker features"
```

Before publishing, verify that no database files, virtual environments, credentials, or generated caches are committed.
