# Final AI Review

## How AI assistance was used

AI assistance was used to compare the repository against the final-project checklist, identify missing release artifacts, propose CI and Docker configuration, update paths after the frontend directory rename, and draft documentation. Each generated change was reviewed against the existing source and tests before acceptance.

## Accepted output

- A GitHub Actions workflow that runs tests, verifies required files, and builds the container.
- A non-root Docker image with a health check.
- A `.dockerignore` that excludes local, generated, sensitive, and assessment-only files.
- `AGENTS.md` with repository-specific working rules.
- Final-project evidence and playbook documents.
- The `static/` to `frontend/` rename and matching FastAPI path update.
- A README section describing final-project deliverables and verification steps.

## Output edited after review

Generated material was adapted to this repository rather than accepted blindly. The workflow uses the actual `requirements.txt` and `pytest` command. The Dockerfile copies the actual `app/` and `frontend/` directories and runs the existing `uvicorn app.main:app` entry point. Documentation describes only behavior present in the codebase.

## Output rejected or avoided

- No new framework, database, frontend build system, or deployment platform was added because it was outside scope.
- No credentials or placeholder secrets were added.
- No unsupported claim of a successful remote GitHub Actions run was made; local tests and the workflow definition are separate evidence.
- No application behavior was rewritten merely to make the repository look more complex.

## Risks identified

1. SQLite writes inside an ephemeral container are not durable unless a volume is mounted.
2. The application creates tables at startup rather than using migrations; this is acceptable for the course project but not ideal for a larger production system.
3. CI proves build and automated-test health, but browser-level end-to-end tests are not included.
4. Date-based overdue behavior depends on the server date.

## Human validation performed

- Checked every required filename and directory against the feedback.
- Reviewed application imports and frontend asset paths after the rename.
- Preserved the existing API contract and tests.
- Confirmed that release documentation does not claim features absent from the code.
- Kept generated files, local databases, and secrets out of version control and Docker context.

## Final judgment

The AI-generated suggestions were useful as a checklist and drafting accelerator, but completion depended on repository inspection, path-aware edits, test execution, and human judgment about scope and evidence quality.
