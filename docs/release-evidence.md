# Release Evidence

## Release candidate

The final-project release candidate is the existing mid-course task tracker plus release-hardening deliverables: GitHub Actions CI, Docker packaging, an agent guidance file, a renamed `frontend/` directory, and final-project documentation.

## Implemented application behavior

- Create, list, update, and delete tasks through the FastAPI API.
- Validate title, status, priority, due date, and up to five normalized tags.
- Compute overdue state for tasks with past due dates that are not complete.
- Filter tasks by search text, priority, exact tag, and overdue state.
- Serve the browser interface from `frontend/`.
- Expose `GET /api/health` for runtime and container health checks.

## Verification commands

```bash
python -m pip install -r requirements.txt
pytest -v
```

Local verification result on 2026-08-04: `6 passed` with pytest. Dependency reinstallation was unavailable in the isolated environment, so the already installed compatible dependencies were used.

```bash
docker build -t ai-assisted-task-tracker .
docker run --rm -p 8000:8000 ai-assisted-task-tracker
```

Expected container checks:

- `http://127.0.0.1:8000/` loads the task tracker.
- `http://127.0.0.1:8000/api/health` returns `{"status":"ok"}`.
- `http://127.0.0.1:8000/docs` loads the API documentation.

Docker was not installed in the local validation environment, so the image definition was inspected and Docker build verification is delegated to the `docker-build` CI job.

## CI evidence

`.github/workflows/ci.yml` runs on pushes to `main`, `mid-course-project`, and `final-project`, and on pull requests. It:

1. installs Python dependencies;
2. runs the pytest suite;
3. verifies all required final-project files and the `frontend/` directory;
4. builds the Docker image in a separate job.

## Release checklist

- [x] CI workflow added.
- [x] Dockerfile added.
- [x] `.dockerignore` added.
- [x] `AGENTS.md` added.
- [x] Required final-project evidence documents added.
- [x] README Final Project section added.
- [x] Frontend moved from `static/` to `frontend/`.
- [x] Application path updated to serve `frontend/`.
- [x] Secrets, databases, virtual environments, and caches excluded.
- [x] Existing application tests retained.

## Rollback

Revert the final-project commit to return to the mid-course version. No database migration is introduced, so rollback does not require data conversion.
