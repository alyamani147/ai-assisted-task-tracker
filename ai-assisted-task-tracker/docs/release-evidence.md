# Release Evidence

## Baseline
- Branch: `final-project`
- Date: 2026-07-28
- Local app run command: `uvicorn app.main:app --reload`
- `/health` result: HTTP 200 with `{"status":"ok"}` during local verification.
- Frontend check: `GET /` returned HTTP 200 and the served HTML contained the Task Tracker title and Kanban board content. The create/edit UI remains present in `frontend/index.html` and `frontend/app.js`.
- Test command: `python -m pytest -v`
- Test result: `7 passed` in `0.26s`; 21 SQLAlchemy deprecation warnings were reported and are documented rather than hidden.
- Scope check: no comments, authentication, notifications, production database, or unrelated UI feature was added.

## CI evidence
- Workflow file: `.github/workflows/ci.yml`
- Trigger: push to `mid-course-project` or `final-project`, and every pull request.
- Python version: exact version `3.13`.
- Dependency command: `python -m pip install -r requirements.txt`
- Test command used by CI: `python -m pytest -v`
- Latest run link or note: add the green GitHub Actions run URL after pushing `final-project`; a local workflow-file review was completed before submission.
- Shortcut check: no `continue-on-error`, no `|| true`, pytest is not skipped, and dependencies are installed before tests.

## Docker evidence
- Build command: `docker build -t ai-task-tracker:final .`
- Run command: `docker run --rm --name ai-task-tracker -p 8000:8000 ai-task-tracker:final`
- `/health` check: `curl -i http://127.0.0.1:8000/health`; expected HTTP 200 and `{"status":"ok"}`.
- Runtime command: exec-form `CMD` starts Uvicorn on `0.0.0.0:8000`.
- Non-root check: the image creates and runs as `appuser` rather than root.
- No-baked-secrets check: `.dockerignore` excludes `.env`, `.env.*`, Git history, databases, logs, caches, tests, and docs; only `app/`, `frontend/`, and `requirements.txt` are copied.
- Local Docker result: Docker was not installed in the repository-generation environment, so no green Docker runtime claim is made here. The submitter must run the build, run, and curl commands locally and replace this note with the actual result before submission.

## Documentation claim-vs-reality log

| Claim checked | Evidence used | Result | Change made, if any |
|---|---|---|---|
| `python -m pytest -v` runs the full suite. | Executed from the repository root. | Confirmed: 7 tests passed. | README uses the verified command. |
| `/health` returns HTTP 200 with `{"status":"ok"}`. | Inspected `app/main.py` and called the endpoint locally. | Confirmed. | Added `/health` as the documented release endpoint while retaining `/api/health` for compatibility. |
| The frontend is served at `/`. | Started Uvicorn, requested `/`, received HTTP 200, and inspected the returned Task Tracker HTML. | Confirmed. | Renamed the source directory from `static/` to required `frontend/` and updated the serving path. |
| Docker does not run as root. | Inspected `Dockerfile` for `USER appuser`. | Confirmed by configuration; runtime verification should be recorded after local build. | Added a dedicated system user. |
| CI cannot silently ignore pytest failure. | Inspected `.github/workflows/ci.yml`. | Confirmed: no failure-suppression setting or shell bypass. | None. |

## Final verification commands
```bash
python -m pytest -v
git diff --check
git grep -nEi '(api[_-]?key|secret|password|token|bearer|BEGIN (RSA|OPENSSH|EC) PRIVATE KEY)' -- . ':!docs/midcourse/*'
docker build -t ai-task-tracker:final .
docker run --rm --name ai-task-tracker -p 8000:8000 ai-task-tracker:final
curl -i http://127.0.0.1:8000/health
```
