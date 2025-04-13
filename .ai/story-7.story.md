# Epic-5 - Story-7
# Documentation Maintenance Rule Creation

**As a** Developer Team
**I want** a Cursor rule that ensures documentation is updated when the API changes
**so that** README, OpenAPI docs, static Markdown docs, and the Postman collection remain accurate and consistent with the implementation.

## Status

Done

## Context

- Follows the creation of various documentation artifacts: README (Story 3), OpenAPI (Story 4), Postman Collection (Story 5), Static Markdown Docs (Story 6).
- Changes to API endpoints (routes, models, parameters) or project structure can cause documentation to become stale.
- This story addresses the need for automated reminders or guidance to maintain documentation consistency, as mentioned in the PRD (Epic 5, Story 7).

## Estimation

Story Points: 2

## Tasks

1.  - [x] **Define Rule Requirements:**
    1.  - [x] Specify triggers for the rule (e.g., changes to endpoint files, model files, potentially project structure files).
    2.  - [x] Define the expected action (e.g., remind the developer/AI to update specific documentation files).
    3.  - [x] Determine the rule type (Agent vs. Auto) and appropriate naming conventions based on `core-rules/rule-generating-agent`.
2.  - [x] **Create Rule File:**
    1.  - [x] Create the file `.cursor/rules/py-rules/fastapi-documentation-maintenance-agent.mdc`.
    2.  - [x] Add the necessary front matter (description, globs, alwaysApply).
    3.  - [x] Write the rule content based on the requirements.
    4.  - [x] Include valid and invalid examples.
3.  - [x] **Verify Rule:**
    1.  - [x] Mentally simulate a scenario where the rule should trigger to ensure it provides the correct guidance.
    2.  - [x] (Optional) Test in a development environment if possible.
4.  - [x] **Update Story Status:** Mark as 'Done'.

## Constraints

- The rule must conform to the standards defined in `core-rules/rule-generating-agent.mdc`.
- The rule should focus on *reminding* or *guiding* updates, not necessarily performing them automatically (unless feasible and desired).

## Data Models / Schema

N/A (Defines a rule, not data models)

## Structure

- Create new file: `.cursor/rules/py-rules/fastapi-documentation-maintenance-agent.mdc`
- Modify existing files: None

## Diagrams

N/A

## Dev Notes

- An 'Agent' rule type seems appropriate, as it requires contextual understanding of *when* documentation needs updates after code changes.
- The description needs to be clear for the agent to know when to apply it.
- Triggers could include modifications to files matching patterns like `app/api/**/*.py`, `app/models/**/*.py`, `app/main.py`.
- The rule should remind the user/AI to check/update `README.md`, `API_DOCUMENTATION.md`, potentially regenerate/update `docs/api_collection.postman_collection.json`, and ensure FastAPI docstrings/models are correct for OpenAPI.

## Chat Command Log

N/A (New Story) 