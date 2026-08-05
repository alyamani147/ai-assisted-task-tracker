# Mini Architecture Decision Record

## Context
The project required two small end-to-end features with visible frontend behavior, backend validation, tests, and documented AI-assisted decisions. The selected features were due dates with overdue filtering and tags with tag filtering.

## Decision
The application uses FastAPI, SQLAlchemy, SQLite, and a dependency-free HTML/CSS/JavaScript frontend.

Due dates are stored as nullable SQL `DATE` values. The backend computes `overdue` in the response using three rules: a due date exists, the date is earlier than today, and the task is not complete. The API supports `?overdue=true` so the behavior is testable independently of the browser.

Tags are exposed through the API as a list but stored in SQLite as a normalized comma-separated string. Input is trimmed, lowercased, deduplicated, limited to five tags, and limited to 24 characters per tag. Exact filtering is implemented with comma-boundary conditions.

## Alternatives considered

### Separate normalized tag table
AI suggested a `tags` table and many-to-many task relationship. This would be a good production design for analytics and tag management, but it adds migrations, joins, relationship handling, and deletion rules. It was rejected as too complex for the assignment scope.

### Compute overdue only in the frontend
This was rejected because browser dates and timezone handling could diverge, and the API could not reliably filter overdue tasks. Backend computation provides one behavior contract.

### Store tags as JSON
SQLite JSON storage was considered, but exact and portable filtering would require database-specific JSON functions. The normalized string keeps the implementation small and testable.

## Consequences
The design is intentionally compact and appropriate for a course project. The tag storage approach would need refactoring for a larger system, especially if tags become shared entities or require analytics. The application also uses local server time for determining today's date, which should become an explicit business timezone in a production deployment.
