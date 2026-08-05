# Release Evidence

## Baseline

- **Branch:** `final-project`
- **Application:** FastAPI task tracker with the browser UI served from `frontend/`.
- **Test command:** `pytest -v`
- **Observed test result (2026-08-04):** 6 tests passed.
- **Health check:** `GET /api/health` returned **HTTP 200** with:

```json
{"status":"ok"}
```

- **Frontend check:** `GET /` returned **HTTP 200**, the HTML contained `<title>Task Tracker</title>`, and `GET /static/styles.css` returned **HTTP 200**.
- **Recorded output:** `evidence/final-pytest.txt` and `evidence/local-runtime-check.txt`.

---

## Claim-versus-reality log

| Documentation claim checked | Evidence used | Observed result | Verdict |
|-----------------------------|---------------|-----------------|---------|
| The automated test suite passes. | Ran `pytest -v`; output saved in `evidence/final-pytest.txt`. | Six tests were collected and all six passed. | ✅ Confirmed |
| The application exposes a working health endpoint. | Started `uvicorn app.main:app --host 127.0.0.1 --port 8011`, then requested `GET /api/health`; output recorded in `evidence/local-runtime-check.txt`. | HTTP 200 with `{"status":"ok"}`. | ✅ Confirmed |
| The frontend is served from the application. | Requested `GET /` and `GET /static/styles.css`; inspected `app/main.py` and `frontend/index.html`. | Both requests returned HTTP 200 and the page title was **Task Tracker**. | ✅ Confirmed |
| The required frontend directory is named `frontend/` and is used by FastAPI. | Inspected the repository structure and `FRONTEND_DIR` in `app/main.py`. | `frontend/` exists and `FRONTEND_DIR` points to it. | ✅ Confirmed |
| CI verifies Docker runtime health, not only image creation. | Reviewed `.github/workflows/ci.yml` and verified the successful GitHub Actions run. | The workflow builds the image, starts the container, checks `GET /api/health`, requires HTTP 200 with `{"status":"ok"}`, and completed successfully. **GitHub Actions run:** https://github.com/alyamani147/ai-assisted-task-tracker/actions/runs/30988687535 | ✅ Confirmed |

---

## Docker build-and-run verification

The Docker image was successfully built and the application was started during the GitHub Actions workflow.

The workflow performed these steps:

```bash
docker build -t ai-assisted-task-tracker:${GITHUB_SHA} .
docker run --detach --name task-tracker-ci -p 8000:8000 ai-assisted-task-tracker:${GITHUB_SHA}
curl http://127.0.0.1:8000/api/health
```

**Observed results:**

- Docker image built successfully.
- Docker container started successfully.
- `GET /api/health` returned **HTTP 200**.
- Response body:

```json
{"status":"ok"}
```

The workflow is configured to fail automatically if:

- the Docker image fails to build,
- the container fails to start,
- `/api/health` does not return HTTP 200,
- or the response body does not contain `"status":"ok"`.

The successful GitHub Actions run confirms that all of these checks passed.

---

## CI run evidence

- **Workflow:** `.github/workflows/ci.yml`
- **Required jobs:** `test` and `docker-runtime`
- **Latest successful GitHub Actions run:**

https://github.com/alyamani147/ai-assisted-task-tracker/actions/runs/30988687535

**Status:** ✅ Passed

The workflow successfully:

- Installed project dependencies.
- Ran the complete test suite.
- Built the Docker image.
- Started the Docker container.
- Verified `GET /api/health` returned **HTTP 200**.
- Verified the response body contained:

```json
{"status":"ok"}
```

This run provides release evidence that the application builds successfully, starts correctly inside a Docker container, and passes the required runtime health check.

---

## Release checklist

- ✅ Required final-project files and directories are present.
- ✅ Tests were run and the output was recorded.
- ✅ Local `/api/health` endpoint returned HTTP 200.
- ✅ Local frontend and stylesheet returned HTTP 200.
- ✅ GitHub Actions built the Docker image.
- ✅ GitHub Actions started the Docker container.
- ✅ GitHub Actions verified `/api/health` returned HTTP 200 with `{"status":"ok"}`.
- ✅ Successful GitHub Actions run recorded:
  https://github.com/alyamani147/ai-assisted-task-tracker/actions/runs/30988687535

---

## Rollback

Revert the final-project release-hardening commit to return to the fully fixed mid-course application. No database migration was introduced, so rollback does not require any data conversion.
