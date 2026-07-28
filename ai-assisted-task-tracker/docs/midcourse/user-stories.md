# User Stories

## Feature 1: Due dates and overdue filter

### Story 1 — Set a due date
As a user, I want to assign an optional due date when creating a task so that I know when the work should be completed.

**Acceptance criteria**
- The create form accepts a valid calendar date.
- A task may be created without a due date.
- The API returns the saved date in ISO `YYYY-MM-DD` format.

### Story 2 — Update a due date
As a user, I want to change or remove a task's due date so that the schedule stays accurate.

**Acceptance criteria**
- Editing a task can replace the existing due date.
- Sending `null` removes the date.
- Updating the date does not modify unrelated fields.

### Story 3 — Identify overdue tasks
As a user, I want overdue open tasks to be clearly marked so that I can prioritize delayed work.

**Acceptance criteria**
- A task is overdue when its due date is before today and its status is not `done`.
- Completed tasks are never reported as overdue.
- Overdue cards show a visible overdue label.

### Story 4 — Filter overdue tasks
As a user, I want to show only overdue tasks so that I can focus on delayed work.

**Acceptance criteria**
- Enabling the overdue filter returns only open overdue tasks.
- Future tasks and completed tasks are excluded.
- An empty result still returns HTTP 200 with an empty list.

**AI assumption corrected:** The first AI suggestion treated every past-due task as overdue, including completed tasks. I corrected the behavior so that `done` tasks are excluded.

## Feature 2: Tags and labels

### Story 1 — Add tags
As a user, I want to add tags to a task so that I can categorize work.

**Acceptance criteria**
- A task accepts zero to five tags.
- Leading and trailing whitespace is removed.
- Tags are normalized to lowercase.
- Duplicate tags are stored only once.

### Story 2 — Validate tags
As a user, I want invalid tags to be rejected so that task metadata remains clean.

**Acceptance criteria**
- Blank tags are rejected with HTTP 422.
- A tag longer than 24 characters is rejected.
- More than five tags are rejected.

### Story 3 — Display tags
As a user, I want tags shown as chips on task cards so that categories are visible at a glance.

**Acceptance criteria**
- Every stored tag is rendered on the card.
- Tasks without tags render normally.
- Tags remain present after updating unrelated task fields.

### Story 4 — Filter by tag
As a user, I want to filter tasks by an exact tag so that similarly named tags do not produce false matches.

**Acceptance criteria**
- Filtering `api` returns tasks tagged `api`.
- Filtering `api` does not return a task tagged `capital`.
- Tag filtering can be combined with search and priority filters.

**AI assumption corrected:** The first AI proposal used a simple substring database filter, which would make `api` match `capital`. I replaced it with comma-boundary checks for exact matching.
