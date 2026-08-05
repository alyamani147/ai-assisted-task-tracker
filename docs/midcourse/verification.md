# Verification

## Baseline check
Before feature work, the intended baseline was:
- Application starts successfully.
- `GET /api/health` returns `{"status":"ok"}`.
- Existing task create, list, update, and delete behavior works.
- Existing tests pass before modifications.

Because this repository was created from scratch for the assignment, the baseline was established after the core CRUD slice and before adding the two selected feature behaviors.

## Automated tests
Run:

```bash
pytest -v
```

Expected result: all tests pass.

New tests include:
1. Create a task with a valid due date and normalized tags.
2. Reject an empty tag.
3. Return only open overdue tasks through the overdue filter.
4. Update due date and tags.
5. Ensure exact tag filtering does not match partial tag text.
6. Combine search, priority, and tag filters.

## Manual browser checks
1. Start the server with `uvicorn app.main:app --reload`.
2. Open `http://127.0.0.1:8000`.
3. Create a task without a due date and confirm it displays normally.
4. Create an open task with yesterday's date and confirm the overdue label appears.
5. Mark that task done and confirm the overdue label disappears.
6. Create a task with `Backend, Urgent`; confirm chips display as `backend` and `urgent`.
7. Filter by `backend`; confirm only exact matching tasks remain.
8. Combine the priority, search, tag, and overdue controls.
9. Clear all filters and confirm the complete board returns.

## Behavior contract before and after refactor
The public behavior contract remained unchanged during the focused refactor:
- POST creates a task and returns HTTP 201.
- PATCH updates only provided fields.
- DELETE returns HTTP 204.
- `tags` is always returned as a list.
- `overdue` is always returned as a boolean.
- Exact tag filtering and overdue filtering remain API query parameters.

## Break Test evidence

### Break Test 1 — Completed past-due task
A deliberately incorrect implementation defined overdue as only `due_date < today`. The overdue-filter test failed because it returned both `Late open` and `Late done`. The rule was corrected by adding `status != "done"` to both response computation and database filtering.

### Break Test 2 — Partial tag match
A deliberately weak filter used `Task.tags.contains("api")`. The regression test failed because it returned both `API task` and `Capital task`. The filter was replaced with exact whole-field and comma-boundary comparisons.

## Known limitations
- Tags are stored as a normalized comma-separated field rather than a relational table.
- Overdue calculation uses the server's local calendar date.
- There is no authentication because it is outside the assignment scope.
