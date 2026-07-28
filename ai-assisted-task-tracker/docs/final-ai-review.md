# Final AI Review and Ownership Evidence

## AGENTS.md guardrails
- Repo-specific stack and commands included: yes.
- Docs-first/read-first guardrail included: yes.
- Unexpected `app/` or `frontend/` edits rule included: yes.
- Scope, data, security, test, and Docker verification rules included: yes.

## Protected-directory corrections
Two small, documentation-supported corrections were made. The frontend directory was renamed from `static/` to the assignment-required `frontend/`, and `app/main.py` was updated to serve that location. A public `/health` route was added because the final brief explicitly grades that endpoint; the existing `/api/health` route was retained as a hidden compatibility alias. No task behavior or new product feature was introduced.

## AI code review mini-log
Review target: `.github/workflows/ci.yml`, `Dockerfile`, and the small `app/main.py` release correction.

| AI comment | Grade | Reason | Verification or decision |
|---|---|---|---|
| Pin a concrete Python version in CI instead of using an unspecified latest version. | Useful | The brief explicitly flags a vague Python version as a dangerous shortcut. | Used Python `3.13` in both CI and Docker, then checked dependency installation and tests. |
| Add `continue-on-error: true` so the workflow still completes when tests fail. | Wrong | This would hide release failures and directly violate the assignment. | Rejected; the test step fails the workflow normally. |
| Use exec-form Docker `CMD` and run as a non-root user. | Useful | Exec form gives clear signal handling, and non-root reduces container privilege. | Implemented `CMD [...]`, created `appuser`, and set `USER appuser`. |
| Rewrite the frontend into a framework to improve maintainability. | Noise | It would be a large unrelated change, add dependencies, and violate scope protection. | Rejected; the vanilla frontend was preserved and only moved to the required directory. |

## AI security mini-review

| Finding | File evidence | Grade | Reason | Next action |
|---|---|---|---|---|
| The application has no authentication. | `app/main.py` task routes | Noise for this release | True in isolation, but authentication is explicitly outside final-project scope and this is a local course app. | Document the limitation; do not add the feature. |
| A local SQLite database could be copied into the image. | `app/database.py`, `Dockerfile`, `.dockerignore` | Valid | Database files can contain submitted task data and should not be baked into an image. | `.dockerignore` excludes `*.db`; Dockerfile does not copy the repository wholesale. |
| Running the container as root is unnecessary. | `Dockerfile` | Valid | The app does not need root privileges at runtime. | Added and selected the non-root `appuser`. |
| Broad write permissions should be used so SQLite always works. | `Dockerfile` | False Positive | World-writable permissions would weaken the image; ownership by the runtime user is sufficient. | Used `chown` for `/app` and did not use `chmod 777`. |
| CI may expose secrets through environment variables. | `.github/workflows/ci.yml` | Noise | The workflow defines no secrets and performs only checkout, dependency installation, and tests. | Keep CI free of unnecessary credentials. |

## Manual security check
I manually listed tracked and untracked files, reviewed `.gitignore` and `.dockerignore`, and searched the repository for credential-like terms and private-key headers. I also checked that the archive did not include `.env`, database, cache, or compiled Python files after cleanup. This matters because the assignment requires a public repository and specifically forbids real credentials, production logs, and personal or customer data.

## One AI output I rejected or corrected
AI suggested that a release-ready application should add authentication before publication. I rejected that suggestion because the assignment explicitly forbids new product features, including authentication. Instead, I documented that the app is a local course project, kept the existing behavior unchanged, and focused on CI, Docker isolation, non-root execution, secret exclusion, and factual release evidence.

## Three AI usage rules
1. Never paste: credentials, tokens, `.env` values, production logs, customer information, or personal data.
2. Always verify: every proposed edit through diff review and the relevant test, command, endpoint, or runtime check.
3. Record AI contributions by: naming the reviewed file, grading the suggestion, and recording whether it was accepted, corrected, downgraded, or rejected.

## Ownership statement
I am comfortable submitting this repository because I can explain the application structure, test behavior, CI workflow, Docker build, and each final-project correction. I ran the verification commands, inspected the relevant diffs, and did not treat AI suggestions as authoritative. I preserved the existing Task Tracker scope and rejected changes that were risky, unnecessary, or outside the brief. The remaining limitations, including local SQLite storage and no authentication, are documented rather than hidden.
