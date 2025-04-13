# Epic-5 - Story-8
Get System Information Endpoint

**As a** system administrator or monitoring tool
**I want** to query a `/system_info` endpoint
**so that** I can retrieve basic system information about the node where the API is running.

## Status

Complete

## Context

This story adds a new GET endpoint `/system_info` to the API as part of expanding its functionality beyond the basic health and hello world endpoints. The goal is to provide readily accessible, non-sensitive system details via the API. This requires reading system information accessible to the user running the FastAPI process (non-root assumed). Adherence to FastAPI best practices, documentation standards (OpenAPI, static docs), and TDD is required.

## Estimation

Story Points: 1

## Tasks

1.  - [x] **Define Pydantic Model:** Create `SystemInfoResponse` model in `app/models/system.py` for the JSON response structure.
    1.  - [x] Include fields for: `current_time`, `os_info` (from `uname`), `cpu_info` (basic model/cores), `memory_info` (total/available), `disk_usage` (relevant mount point), `uptime`.
2.  - [x] **Implement Endpoint Logic:** Create the `/system_info` GET endpoint in `app/api/v1/endpoints/system.py`.
    1.  - [x] Implement helper function(s) (e.g., in `app/core/system_utils.py`) to gather system information using standard Python modules (`os`, `platform`, `psutil`, `datetime`) accessible by a non-root user.
    2.  - [x] Ensure error handling for cases where information cannot be retrieved.
    3.  - [x] Use the `SystemInfoResponse` model for the response.
3.  - [x] **Register Endpoint:** Add the new system router to `app/main.py`.
4.  - [x] **Write Unit Tests:** Create tests in `app/tests/test_system.py`.
    1.  - [x] Test successful retrieval of system information.
    2.  - [x] Mock system calls to ensure test isolation and repeatability.
    3.  - [x] Test endpoint registration and response model.
5.  - [x] **Update Documentation:**
    1.  - [x] Ensure OpenAPI documentation (Swagger/ReDoc) is automatically generated via FastAPI docstrings and the Pydantic model.
    2.  - [x] Update static documentation (`API_DOCUMENTATION.md`) with details about the new endpoint.
    3.  - [x] ~~Regenerate/Update Postman collection (`postman_collection.json`).~~ (Manual step required/Separate task)
6.  - [x] **Run All Tests:** Execute `make test` to ensure all tests pass, including previous ones.

## Constraints

- The endpoint must only retrieve information accessible by a non-root user.
- Response time should remain low (<500ms under normal load).
- Must use standard Python libraries (`os`, `platform`, `psutil`, `datetime`) where possible. `psutil` might need to be added as a dependency.
- Follow established FastAPI structure and best practices.

## Data Models / Schema

```python
# app/models/system.py
from pydantic import BaseModel
from datetime import datetime

class MemoryInfo(BaseModel):
    total: str
    available: str
    percent_used: float

class DiskInfo(BaseModel):
    total: str
    used: str
    free: str
    percent_used: float

class SystemInfoResponse(BaseModel):
    current_time: datetime
    os_info: str
    cpu_info: str # Simplified for now, e.g., "Model Name, X Cores"
    memory: MemoryInfo
    disk: DiskInfo # For root filesystem '/'
    uptime: str
```

## Structure

- New endpoint: `app/api/v1/endpoints/system.py`
- New model: `app/models/system.py`
- New utility functions: `app/core/system_utils.py` (if needed)
- New tests: `app/tests/test_system.py`
- Update `app/main.py` to include the new router.
- Update `API_DOCUMENTATION.md`, `postman_collection.json`.

## Diagrams

N/A for this story.

## Dev Notes

- Need to add `psutil` to `requirements.txt`.
- Focus on gracefully handling errors if certain system info cannot be read due to permissions or OS differences.
- Ensure the `current_time` reflects the server's time in a standard format (e.g., ISO 8601).
- Postman collection update needs to be done manually or via a separate process.

## Chat Command Log

- User: crea una nueva story la 8 para un nuevo endpoint siguiendo @workflow-agile-manual.mdc usando @modes.json el nuevo endpoint es un get que devuelve info del sistema busca en internet toda la info que puede devolver el endpoint para informar del nodo donde se esta ejecutando ten en cuenta que sera usuario no root , el formato de respuesta sera json y debera incluir la hora actual, aplica todas las reglas de fastapi durante el desarrollo y tambien el restor de reglas
- User: continua

## Examples

N/A 