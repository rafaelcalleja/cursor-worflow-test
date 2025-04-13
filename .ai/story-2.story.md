# Epic-1 - Story-2
Hello World Endpoint

**As a** Developer/User
**I want** a working `/hw` endpoint
**so that** I can get a basic "Hello World" message from the API

## Status

Complete

## Context

This story implements the second core feature of the MVP, the `/hw` endpoint, as defined in the approved PRD (`.ai/prd.md`) and architecture (`.ai/arch.md`). This follows the completion of Story 1 (Project Setup & Health Check). This story corresponds to 'Story 2' under 'Epic 1: Story List (MVP)' in the PRD.

## Estimation

Story Points: 1 (Initial estimate)

## Tasks

1.  - [x] Implement the `/hw` GET endpoint in `api/endpoints.py`.
    1.  - [x] Define the endpoint function.
    2.  - [x] Return 200 OK status and JSON `{"message": "Hello World"}`.
    3.  - [x] Ensure the endpoint is registered with the main FastAPI app router.
2.  - [x] Add unit tests for the `/hw` endpoint in `tests/test_endpoints.py`.
    1.  - [x] Write test case to assert 200 status code for `/hw`.
    2.  - [x] Write test case to assert correct JSON response `{"message": "Hello World"}`.

## Constraints

- API response for `/hw` should be < 500ms under normal load (as per PRD).
- Adhere to the project structure defined in `.ai/arch.md`.
- Technology stack as defined in PRD/Arch (Python, FastAPI, Docker, Pytest).

## Data Models / Schema

`/hw` Response Schema (from PRD/Arch):
```json
{
  "message": "string" // e.g., "Hello World"
}
```

## Structure

Uses the existing project structure outlined in `.ai/arch.md`:
```
/app
├── main.py
├── api/
│   ├── __init__.py
│   └── endpoints.py
├── tests/
│   ├── __init__.py
│   └── test_endpoints.py
├── Dockerfile
├── requirements.txt
└── README.md
```

## Diagrams

N/A

## Dev Notes

- Follow TDD principles: write tests concurrently or just before implementation.
- Ensure the new endpoint is correctly added to the router in `app/main.py` if necessary (depending on implementation in `endpoints.py`).

## Chat Command Log

(Empty) 