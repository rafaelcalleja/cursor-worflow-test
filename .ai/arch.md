# Architecture for API Rest Hello World

Status: Draft

## Technical Summary

This document outlines the technical architecture for the "API Rest Hello World" service. The initial MVP focuses on creating a simple, containerized REST API using Python and FastAPI. It will provide two basic endpoints: `/health` for health checks and `/hw` for a "Hello World" message. The architecture prioritizes simplicity, ease of deployment via Docker, and adherence to modern Python best practices, laying the groundwork for future expansion.

## Technology Table

| Technology | Description                                  | Choice Rationale (from PRD)   |
| :--------- | :------------------------------------------- | :---------------------------- |
| Language   | Python                                       | Fast, modern, easy to learn   |
| Framework  | FastAPI                                      | High performance, async, docs |
| Deployment | Docker                                       | Containerization standard     |
| Testing    | Pytest                                       | Robust Python testing         |
| Server     | Uvicorn (with Gunicorn for production later) | Standard ASGI server for FastAPI |

## Architectural Diagrams

```mermaid
graph TD
    A[Client] --> B(API: FastAPI on Uvicorn);
    B -- GET /health --> C{Health Check Logic};
    B -- GET /hw --> D{Hello World Logic};
    C --> E[Response: {"status": "healthy"}];
    D --> F[Response: {"message": "Hello World"}];
```

*Diagram shows basic client interaction with the two MVP endpoints.*

## Data Models, API Specs, Schemas, etc...

*(Schemas defined in PRD)*

### `/health` Response Schema
```json
{
  "status": "string" // e.g., "healthy"
}
```

### `/hw` Response Schema
```json
{
  "message": "string" // e.g., "Hello World"
}
```

## Project Structure

```
/app
├── main.py        # FastAPI app definition, routers
├── api/
│   ├── __init__.py
│   └── endpoints.py # Endpoint implementations (/health, /hw)
├── tests/
│   ├── __init__.py
│   └── test_endpoints.py # Unit tests for endpoints
├── Dockerfile     # Docker build instructions
├── requirements.txt # Python dependencies
└── README.md      # Project README
```

## Infrastructure

- Local Development: Docker Desktop or equivalent.
- Deployment Target (Initial): Single Docker container. Future iterations might involve cloud platforms (e.g., AWS ECS, Google Cloud Run).

## Deployment Plan

- **Build:** Build a Docker image using the `Dockerfile`.
  ```bash
  docker build -t rest-api-hello-world .
  ```
- **Run:** Run the Docker container, mapping the necessary port (e.g., 8000).
  ```bash
  docker run -d -p 8000:8000 rest-api-hello-world
  ```
- A simple script (`deploy.sh`) could automate these steps for the MVP.

## Change Log

| Change        | Story ID | Description                  |
| :------------ | :------- | :--------------------------- |
| Initial draft | N/A      | Initial architecture draft | 