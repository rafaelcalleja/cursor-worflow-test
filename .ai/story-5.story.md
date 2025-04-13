# Epic-5 - Story-5
# Postman Collection Generation

**As a** Developer / API Consumer
**I want** a Postman collection for the API
**so that** I can easily send requests to the available endpoints for testing or interaction.

## Status

Done

## Context

- Follows the completion of Story 4 (API Auto-Documentation Setup).
- The API has `/api/v1/health` and `/api/v1/hw` GET endpoints.
- FastAPI generates an OpenAPI specification (available at `/openapi.json` when running).
- This story addresses the requirement from the PRD (`.ai/prd.md`, Epic 5, Story 5).

## Estimation

Story Points: 1

## Tasks

1.  - [x] **Create Postman Collection File:**
    1.  - [x] Define the basic Postman collection structure (info block).
    2.  - [x] Add a request item for the `GET /api/v1/health` endpoint.
    3.  - [x] Add a request item for the `GET /api/v1/hw` endpoint.
    4.  - [x] Ensure request URLs, methods, and names are correct.
    5.  - [x] Save the collection as a JSON file (e.g., `docs/api_collection.postman_collection.json`).
2.  - [x] **Verify Collection (Manual):**
    1.  - [x] Import the generated JSON file into Postman.
    2.  - [x] Send requests for both endpoints to confirm they work against a running instance of the API.
3.  - [x] **Update Story Status:** Mark as 'Done'.

## Constraints

- The collection must be in Postman Collection Format v2.1.0.
- Must accurately reflect the available MVP endpoints.

## Data Models / Schema

N/A (Describes requests, not data models)

## Structure

- Creates a new file: `docs/api_collection.postman_collection.json`

## Diagrams

N/A

## Dev Notes

- Generating this manually for the two simple endpoints is feasible for now.
- For more complex APIs, automating this from the `/openapi.json` endpoint using tools like `openapi-to-postmanv2` or Postman's import feature would be better.
- Assumes the API runs on `http://localhost:8000` as per previous setup.

## Chat Command Log

- User: @story-1.story.md y @story-2.story.md estan completadas los siguientes pasos son las siguientes historia sigue el @workflow-agile-manual.mdc usando @modes.json
- User: continua con el @workflow-agile-manual.mdc usando @modes.json
- User: hay que revisar  @story-3.story.md  y compeltar todos los pasos siguiendo el @workflow-agile-manual.mdc usando @modes.json 