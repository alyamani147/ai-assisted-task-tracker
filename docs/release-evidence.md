# Release Evidence

## Baseline

- **Branch:** `final-project`
- **Application:** FastAPI task tracker with the browser UI served from `frontend/`.
- **Test command:** `pytest -v`
- **Observed test result on 2026-08-04:** `6 passed`.
- **Health check:** `GET /api/health` returned HTTP `200` with `{"status":"ok"}`.
- **Frontend check:** `GET /` returned HTTP `200`, the HTML contained `<title>Task Tracker</title>`, and `GET /static/styles.css` returned HTTP `200`.
- **Recorded output:** `evidence/final-pytest.txt` and `evidence/local-runtime-check.txt`.

## Claim-versus-reality log

| Documentation claim checked | Evidence used | Observed result | Verdict |
|---|---|---|---|
| “The automated test suite passes.” | Ran `pytest -v`; full output is saved in `evidence/final-pytest.txt`. | Six tests were collected and all six passed. | **Confirmed** |
| “The application exposes a working health endpoint.” | Started `uvicorn app.main:app --host 127.0.0.1 --port 8011`, then requested `GET /api/health`. Output is in `evidence/local-runtime-check.txt`. | HTTP `200`; body `{"status":"ok"}`. | **Confirmed** |
| “The frontend is served from the application.” | Requested `GET /` and `GET /static/styles.css` from the running app; inspected `app/main.py` and `frontend/index.html`. | Both requests returned HTTP `200`; the page title was `Task Tracker`. | **Confirmed** |
| “The required frontend directory is named `frontend/` and is used by FastAPI.” | Inspected the repository tree and `FRONTEND_DIR` in `app/main.py`. | `frontend/` exists and `FRONTEND_DIR = ... / "frontend"`. | **Confirmed** |
| “CI verifies Docker runtime health, not only image creation.” | Inspected `.github/workflows/ci.yml`, job `docker-runtime`. | The job builds the image, starts `task-tracker-ci`, polls `/api/health`, requires HTTP `200`, checks the response body, and writes the observed result to the Actions step summary. | **Confirmed in workflow definition; remote run evidence must come from the pushed commit** |

## Docker build-and-run verification

The repository now contains an executable CI runtime check rather than an image-build-only check. The `docker-runtime` job performs these observed checks on GitHub's Ubuntu runner:

```bash
docker build -t ai-assisted-task-tracker:${GITHUB_SHA} .
docker run --detach --name task-tracker-ci -p 8000:8000 ai-assisted-task-tracker:${GITHUB_SHA}
curl http://127.0.0.1:8000/api/health
```

The job fails unless the endpoint returns HTTP `200` and the response contains `"status":"ok"`. It also records the image name, container name, HTTP status, and response body in the GitHub Actions job summary.

**Local environment note:** Docker was not available in the environment used to prepare this archive, so no local Docker success is claimed. The required observed Docker result must be taken from the green `docker-runtime` job after this branch is pushed.

## CI run evidence

- **Workflow:** `.github/workflows/ci.yml`
- **Required successful jobs:** `test` and `docker-runtime`
- **Actions page:** `https://github.com/alyamani147/ai-assisted-task-tracker/actions/workflows/ci.yml`
- **Run status for this revised commit:** add the latest green run link after pushing the revised `final-project` branch.

A valid completion note after the push is:

> GitHub Actions ran successfully for the latest `final-project` commit. Both the `test` and `docker-runtime` jobs were green; the Docker job started the container and recorded HTTP 200 with `{"status":"ok"}` from `/api/health`.

This line must only be used after the run is actually green.

## Release checklist

- [x] Required final-project files and directories are present.
- [x] Tests were run and the output was recorded.
- [x] The local `/api/health` endpoint returned HTTP 200.
- [x] The local frontend and stylesheet returned HTTP 200.
- [x] The CI workflow builds and starts the Docker image.
- [x] The CI workflow checks the container health endpoint and response body.
- [ ] Push the revised `final-project` branch and add the latest green Actions run link above.

## Rollback

Revert the final-project release-hardening commit to return to the fully fixed mid-course application. No database migration was introduced, so rollback does not require data conversion.
