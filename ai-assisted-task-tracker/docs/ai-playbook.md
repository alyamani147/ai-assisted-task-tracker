# My AI Playbook

## When I reach for AI first
I use AI early for bounded tasks where the output can be checked quickly: drafting test cases from an existing behavior contract, reviewing a small diff, explaining an error log, proposing a CI or Docker skeleton, and turning rough notes into structured documentation. During this course, AI was most useful when I gave it real files, exact constraints, and a clear definition of done.

## When I do not reach for AI first
I first inspect the code, logs, current diff, and documentation when context is incomplete or the change affects security, infrastructure, data, or public behavior. I also avoid using AI first when the point of the task is to learn the underlying mechanism myself. For incidents or customer data, I sanitize the material before any AI use.

## My non-negotiables
- Never paste secrets, tokens, `.env` values, production logs, personal data, or customer information.
- Never submit a line, command, dependency, or configuration choice I cannot explain.
- Never weaken tests or hide failures to make a pipeline green.
- Keep AI changes small and inside the requested scope.
- Verify claims against the repository or a running system.

## My review rules
I read the relevant files before prompting, ask for focused output, inspect the complete diff, and run the smallest relevant check before the full suite. I grade findings instead of accepting them: useful/valid, noise/false positive, or wrong. I reject suggestions that add scope, remove safeguards, or rely on assumptions not supported by evidence. For CI and Docker, I check exact versions, dependency installation, runtime user, copied files, entrypoint, and failure behavior.

## What I am still figuring out
I am still refining when to use one broad review prompt versus several narrow prompts, and how much AI-generated documentation is helpful before it becomes repetitive. In a team setting, I would also want agreement on which AI contributions must be recorded in pull requests and which tools are approved for internal code.

## Decision Card
| Situation | My default decision |
|---|---|
| New feature | Define scope and acceptance criteria first; use AI only after reading the current design. |
| Code review | Ask for three evidence-backed findings, then grade each one myself. |
| Debugging | Start from logs, reproduction steps, and a failing test; do not guess from symptoms alone. |
| Infrastructure | Use AI for a draft, then verify every flag, permission, copied file, and failure mode. |
| Never paste | Secrets, credentials, production logs, customer data, or personal data. |
| One rule | No evidence, no acceptance. |
