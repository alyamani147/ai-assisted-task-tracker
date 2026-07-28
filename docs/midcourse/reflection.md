# Reflection

I used an AI coding assistant for planning, implementation drafts, test ideas, and review. Its strongest contribution was turning a broad feature request into small vertical slices. For due dates, it separated the work into database storage, schema validation, API filtering, frontend rendering, and verification. This made it easier to test each layer before moving to the next. For tags, it generated useful edge cases such as whitespace, duplicates, excessive tag counts, and unrelated updates preserving existing values.

AI helped most when I asked it to write a failing Break Test before suggesting a correction. The exact-tag test exposed a subtle problem: a substring filter for `api` also matched `capital`. That defect might have survived a simple happy-path test. Keeping the failing test and then changing the query produced a clearer behavior contract and a useful regression test.

AI slowed me down when its first design proposed a normalized tag table with a many-to-many relationship. That design is reasonable for a larger application, but it introduced migrations, joins, relationship serialization, and deletion behavior that were not necessary for this assignment. I rejected it and used a constrained comma-separated representation while preserving a list-based API.

My review also changed the overdue behavior. The initial output treated every task with a past due date as overdue. I noticed that completed work should not remain in an overdue queue, so I added the `status != done` rule to both the computed response field and the database filter. I then added a test that included a completed past-due task.

The main lesson was that prompt quality affected output quality, but review mattered more than prompt length. Specific constraints produced smaller, more relevant changes. Tests provided evidence when an AI assumption was wrong. I accepted generated code only after tracing the data flow, running the tests, and checking the feature manually in the browser.
