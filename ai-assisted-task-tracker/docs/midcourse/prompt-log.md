# Prompt Log

## Feature 1: Due dates and overdue filter

### Prompt 1 — Planning
**Prompt:** "Plan the smallest end-to-end implementation for optional task due dates and an overdue filter in a FastAPI and vanilla JavaScript Kanban app. Include the data model, validation, API behavior, UI changes, and tests. Do not add reminders or notifications."

**AI response summary:** Suggested a nullable date field, response-level overdue boolean, query parameter, date control in the modal, card indicator, and tests.

**Decision:** Accepted the general plan. Rejected notifications and scheduling as out of scope.

### Prompt 2 — Strengthened implementation prompt
**Weak prompt:** "Add due dates to my app."

**Rewritten prompt:** "Add a nullable SQLAlchemy `Date` field named `due_date`; accept ISO dates on POST and PATCH; compute overdue only when `due_date < today` and status is not `done`; implement `GET /api/tasks?overdue=true`; preserve all existing fields; return 422 for malformed dates; and provide focused pytest tests before editing the frontend."

**AI response summary:** Produced schema, route, and test changes.

**Decision:** Edited the overdue rule because the first response included completed tasks.

### Prompt 3 — Frontend integration
**Prompt:** "Add a date input to the existing task modal, show a clear overdue label on cards, and add an overdue-only checkbox above the Kanban board. Keep all three columns visible and preserve the empty state. Use no frontend framework."

**Decision:** Accepted with minor naming and accessibility edits.

## Feature 2: Tags and labels

### Prompt 1 — Planning
**Prompt:** "Design a scoped tags feature for this assignment. The API should expose a list of strings, support create and update, validate clean values, and allow exact tag filtering. The UI should use comma-separated input and chips. Avoid a many-to-many schema unless it is essential."

**AI response summary:** Proposed normalization, limits, chips, and query filtering. It also suggested a normalized database table.

**Decision:** Rejected the many-to-many table as unnecessary for this scope.

### Prompt 2 — Validation and storage
**Prompt:** "Implement tags with these constraints: trim and lowercase values, reject blanks, remove duplicates, allow at most five tags, limit each tag to 24 characters, expose tags as `list[str]`, and persist them in a simple SQLite-compatible representation. Add tests for valid tags and rejected blank tags."

**Decision:** Accepted the validator. Edited storage conversion so API responses always remain lists.

### Prompt 3 — Break Test correction
**Prompt:** "Write a failing test proving that filtering for tag `api` must not match a task tagged `capital`. Then fix only the filtering logic without changing the public API."

**AI response summary:** The initial substring query failed the test. AI suggested delimiter-aware conditions.

**Decision:** Accepted the boundary-based filter and retained the test as regression evidence.
