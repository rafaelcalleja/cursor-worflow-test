# Epic-5 - Story-6
# Comprehensive Static API Documentation (Markdown)

**As a** Developer or API Consumer
**I want** a detailed static Markdown documentation file for the API within the repository
**so that** I can easily understand how to set up, use, and interact with the API, including usage examples (like curl or Postman) and detailed endpoint descriptions, independent of the running application.

## Status

Done

## Context

- Existing auto-generated FastAPI documentation (`/docs`, `/redoc`) via Story-4 provides a basic overview but is not sufficient for comprehensive understanding or offline use.
- Need a persistent, detailed guide within the codebase itself.
- This addresses the request for more thorough documentation beyond the auto-generated OpenAPI spec.
- Follows the completion of Story 5 (Postman Collection).

## Estimation

Story Points: 3

## Tasks

1.  - [x] **Define Documentation Structure:**
    1.  - [x] Research and finalize the optimal structure and sections for the Markdown file (e.g., Introduction, Authentication, Local Setup, Endpoint Reference, Data Models, Usage Examples, Error Handling, Versioning).
2.  - [x] **Create Initial File:**
    1.  - [x] Create a root-level file named `API_DOCUMENTATION.md` (or similar).
    2.  - [x] Populate the file with the defined section headers.
3.  - [x] **Document Existing Endpoints:**
    1.  - [x] Add detailed descriptions for `/api/v1/health` and `/api/v1/hw`.
    2.  - [x] Include request/response formats, parameters (if any), and potential status codes.
4.  - [x] **Document Data Models:**
    1.  - [x] Add details for `HealthStatus` and `Message` models from `app/models/response.py`.
    2.  - [x] Explain each field, type, and validation rule.
5.  - [x] **Add Usage Examples:**
    1.  - [x] Provide clear `curl` examples for each endpoint.
    2.  - [x] Optionally, include instructions or a link to a Postman collection (from Story 5).
6.  - [x] **Add Setup & Authentication Info:**
    1.  - [x] Document steps for setting up the project locally (referencing `README.md` if applicable).
    2.  - [x] Detail the authentication mechanism (if any is planned or implemented later).
7.  - [x] **Review and Refine:**
    1.  - [x] Ensure clarity, accuracy, and completeness based on best practices.

## Constraints

- Documentation must be a static Markdown file committed to the repository.
- Must be comprehensive and easy to navigate.
- Should complement, not just duplicate, the existing `README.md`.

## Data Models / Schema

- References existing models:
  - `app.models.response.HealthStatus`
  - `app.models.response.Message`
- Will define the structure of the `API_DOCUMENTATION.md` file itself.

## Structure

- Create new file: `API_DOCUMENTATION.md`
- Modify existing files: None (initially)

## Diagrams

N/A

## Dev Notes

- This story deviates from solely relying on FastAPI's auto-documentation.
- The Markdown format ensures accessibility and version control alongside the code.
- Consider tools that might help generate parts of this from code/OpenAPI spec later, but the primary goal is a curated, static document.
- **Action:** Need to update `.ai/prd.md` to reflect this new story in the backlog.

## Chat Command Log

- User: {Previous user query about needing markdown documentation}
- Assistant: {My previous response attempting to create story-5}
- User: ya existe @story-5.story.md una nueva historia seria la 6 