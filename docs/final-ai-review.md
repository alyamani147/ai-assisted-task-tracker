# Final AI Review

## AGENTS.md guardrail confirmation

Before accepting AI-assisted changes, I checked them against `AGENTS.md`.

- **Scoped changes:** the work only adds release hardening, evidence, and the required `frontend/` path; it does not replace the framework or database.
- **No secrets or generated state:** no credentials, `.env` files, virtual environments, caches, or SQLite database files are included.
- **Tests and packaging checks:** `pytest -v` was run locally, and CI now builds and starts the Docker image before checking `/api/health`.
- **Behavior preserved:** exact-tag filtering and the rule that completed tasks are not overdue remain covered by `tests/test_tasks.py`.
- **Documentation synchronized:** README, CI, Docker instructions, and evidence documents describe the current repository structure.

## AI code review mini-log

| AI review comment | Grade | Reason and decision |
|---|---|---|
| “Renaming `static/` to `frontend/` requires updating the FastAPI filesystem path.” | **Useful** | Confirmed in `app/main.py`: `FRONTEND_DIR` now points to `frontend/`. The `/static` URL mount remains intentionally unchanged because it is a URL path, not the folder name. |
| “Replace SQLite with PostgreSQL before release.” | **Noise** | This is outside the course scope and would add infrastructure without improving the required deliverables. SQLite is retained and its container persistence limitation is documented. |
| “The original Docker CI job proves runtime health because the image builds successfully.” | **Wrong** | A successful build does not prove the process starts or that `/api/health` responds. The workflow was corrected to run a container, poll the endpoint, assert HTTP 200, and record the response. |
| “Use `innerHTML` directly for task titles and descriptions.” | **Wrong** | User-controlled values must be escaped. `frontend/app.js` keeps `escapeHtml()` around title, description, and tags. |

## AI security mini-review

| Finding with file evidence | Grade | Reason | Next action |
|---|---|---|---|
| `frontend/app.js` renders task fields inside template strings, which can create an XSS risk. | **Valid** | The risk is real when using `innerHTML`, but the current implementation applies `escapeHtml()` to title, description, and every tag before insertion. | Keep the escaping function and add a frontend security test if a browser test framework is introduced. |
| `app/database.py` uses `sqlite:///./task_tracker.db`, so container data is stored in the writable container layer. | **Valid** | Data is lost when an ephemeral container is removed unless a volume is mounted. This is a durability issue, not a secret exposure. | Document volume usage for persistent deployments or move the database URL to configuration in a later production-focused iteration. |
| `app/main.py` uses SQLAlchemy query expressions built from request parameters and may be vulnerable to SQL injection. | **False Positive** | The filters use SQLAlchemy expressions and bound parameters rather than concatenating raw SQL. | No code change required; continue avoiding raw SQL constructed from user input. |
| `Dockerfile` exposes port 8000, which exposes the application publicly. | **Noise** | `EXPOSE` is metadata and does not publish a port by itself. Publishing is controlled by the runtime command or deployment platform. | No change required. |
| `Dockerfile` might run as root. | **False Positive** | The file creates `appuser` with UID 10001 and switches with `USER appuser` before startup. | Keep the non-root user and verify it if container security tests are added. |

## Three AI usage rules

1. **Verify every generated claim:** compare AI output with source files, tests, commands, endpoint responses, or CI output before documenting it as true.
2. **Reject unnecessary scope:** do not accept framework migrations, infrastructure changes, or complexity that is unrelated to the stated requirement.
3. **Treat security feedback as hypotheses:** grade each finding using file evidence, explain why it is valid or not, and record a concrete next action.

## Ownership statement

I reviewed and accepted responsibility for every file in this submission. AI helped identify missing deliverables, draft configurations, and structure the evidence, but I checked those suggestions against the repository and observed application behavior. I corrected the Docker workflow after recognizing that image build success alone did not prove runtime health. I understand the application, its tests, its packaging, and the remaining SQLite persistence limitation. I would be able to explain or modify these changes without relying on the original AI output.
