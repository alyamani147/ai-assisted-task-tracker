# AI-Assisted Development Playbook

## 1. Establish the baseline

Before asking AI to change code:

```bash
git status
pytest -v
find . -maxdepth 3 -type f | sort
```

Record what already works and identify the exact acceptance criteria.

## 2. Give grounded prompts

Include the relevant file contents, failing output, expected behavior, constraints, and definition of done. Ask for a small patch rather than a broad rewrite.

Example:

> The FastAPI app currently serves assets from `static/`, but the assignment requires `frontend/`. Rename the directory, update only the necessary path references, preserve `/static/...` browser URLs, and identify tests or checks needed to prove nothing broke.

## 3. Inspect before accepting

Review generated changes for:

- invented files, dependencies, commands, or APIs;
- accidental behavior changes;
- missing error handling or validation;
- secrets or machine-specific paths;
- documentation claims not supported by code;
- unnecessary complexity.

## 4. Test from evidence

Run the narrowest relevant test first, then the full suite:

```bash
pytest -v tests/test_tasks.py
pytest -v
```

For packaging changes:

```bash
docker build -t ai-assisted-task-tracker .
docker run --rm -p 8000:8000 ai-assisted-task-tracker
```

Verify `/`, `/api/health`, and `/docs` manually when possible.

## 5. Use deliberate break tests

Temporarily introduce a controlled fault, confirm the test catches it, then restore the correct implementation and rerun the suite. This demonstrates that tests are meaningful rather than merely green.

## 6. Keep an acceptance log

For each meaningful AI suggestion, record whether it was:

- accepted unchanged;
- accepted after editing;
- rejected;
- deferred, with the reason.

## 7. Protect the repository

Before committing:

```bash
git diff --check
git status --short
pytest -v
```

Confirm that `.env`, tokens, database files, virtual environments, caches, and editor settings are not staged.

## 8. Complete the release checklist

A release is ready when application tests pass, CI exists, the container builds, required documents are present, README instructions are accurate, and the branch contains only intentional changes.
