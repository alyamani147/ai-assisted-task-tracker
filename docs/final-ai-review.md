# Final AI Review

## AGENTS.md guardrail confirmation

I reviewed the repository using the guidance in `AGENTS.md` before making final changes. I confirmed that required project files were present, the repository structure matched the assignment requirements, and changes remained limited to the final-project deliverables. I manually reviewed every AI-generated change before committing it.

---

## AI code review mini-log

| AI Comment | Grade | Reason |
|------------|-------|--------|
| Rename `static/` to `frontend/` to match the assignment requirements. | Useful | This was a genuine assignment requirement and improved compliance. |
| Add a Docker health check to the CI workflow. | Useful | The original workflow only built the image. Adding a runtime check satisfied the project requirement. |
| Replace placeholder evidence in the documentation with observed results. | Useful | This improved the quality and accuracy of the release documentation. |
| Rewrite several comments for consistency. | Noise | These changes were stylistic and did not improve correctness or functionality. |

---

## AI security mini-review

| Finding | File Evidence | Grade | Reason | Next Action |
|---------|---------------|-------|--------|-------------|
| No secrets are committed to the repository. | Repository review | Valid | No API keys or credentials were found. | Continue checking before every release. |
| Debug mode should not be enabled in production. | `app/main.py` | Valid | Development settings should not be used for production deployments. | Keep production configuration separate. |
| User input should always be validated. | `app/main.py` | Valid | Validation reduces the risk of malformed requests. | Continue using FastAPI validation. |
| Missing authentication. | Entire project | False Positive | Authentication is outside the scope of this coursework project. | No action required for this assignment. |

---

## Manual security check

After completing the AI-assisted review, I manually inspected the project for common security issues.

Checks performed:

- Verified that no passwords, API keys, or secrets are stored in the repository.
- Confirmed that the application only exposes the expected endpoints.
- Confirmed that no sensitive files are included in the Docker image.
- Reviewed the `.gitignore` and `.dockerignore` files.
- Verified that the Docker container exposes only the required application port.
- Confirmed the `/api/health` endpoint returns only a simple status response and does not leak sensitive information.

No additional security issues were found during the manual review.

---

## One AI output I rejected or corrected

One AI suggestion recommended documenting Docker verification using expected output because Docker was unavailable locally.

I rejected this suggestion because the assignment required observed evidence rather than expected behaviour.

Instead, I updated the GitHub Actions workflow so it actually builds the Docker image, starts the container, verifies that `/api/health` returns HTTP 200 with `{"status":"ok"}`, and then linked the successful GitHub Actions run as evidence.

---

## Three AI usage rules

1. Never accept AI-generated code without reading and understanding it first.
2. Always verify AI-generated documentation against the actual repository and application behaviour.
3. Use AI to speed up development, but make the final technical decisions myself.

---

## Ownership statement

Although AI assisted with brainstorming, reviewing code, improving documentation, and identifying missing assignment requirements, I reviewed every suggested change before accepting it. I verified the application by running the tests, checking the API endpoints, and confirming that the required project files were present. I corrected AI suggestions when they did not satisfy the assignment requirements, particularly around release evidence and Docker verification. I take responsibility for the final implementation, documentation, testing, and submission of this project.
