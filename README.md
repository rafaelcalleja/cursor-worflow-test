# Simple FastAPI Service

A minimal REST API service built with FastAPI, providing basic health check and "Hello World" endpoints.

## Table of Contents

- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Application](#running-the-application)
  - [Using Docker](#using-docker)
  - [Running Locally](#running-locally)
- [Running Tests](#running-tests)
- [API Endpoints](#api-endpoints)
- [Technology Stack](#technology-stack)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
.
├── .ai/              # AI-related artifacts (PRD, Stories)
├── app/              # Main application source code
│   ├── __init__.py
│   ├── main.py       # FastAPI app instantiation and middleware
│   └── api/
│       └── v1/
│           ├── __init__.py
│           └── endpoints/
│               ├── __init__.py
│               └── endpoints.py # API endpoint definitions (/health, /hw)
├── tests/            # Unit and integration tests
├── .gitignore
├── Dockerfile        # Docker configuration (Needs implementation)
├── Makefile          # Project commands (e.g., test)
├── README.md         # This file
└── requirements.txt  # Python dependencies
```

*(Note: This structure might evolve as the project grows.)*

## Getting Started

### Prerequisites

- Python 3.9+
- Docker (Optional, for containerized execution)
- pip (Python package installer)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Create and activate a virtual environment (Recommended):**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

### Using Docker

*(Note: The `Dockerfile` needs to be implemented first. These are standard commands assuming a typical FastAPI setup exposing port 8000.)*

1.  **Build the Docker image:**
    ```bash
    docker build -t simple-fastapi-service .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -d -p 8000:8000 --name simple-fastapi-app simple-fastapi-service
    ```
    The application will be accessible at `http://localhost:8000`.

### Running Locally

Use `uvicorn` to run the application directly:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```
The application will be accessible at `http://localhost:8000`. The `--reload` flag enables auto-reloading on code changes.

## Running Tests

Execute the test suite using `pytest`:

```bash
pytest
```
*(Alternatively, use `make test` if configured in the `Makefile`)*

## API Endpoints

The following endpoints are available under the `/api/v1` prefix:

- **GET `/api/v1/health`**: Returns the health status of the service.
  - Response: `{"status": "healthy"}`
- **GET `/api/v1/hw`**: Returns a simple "Hello World" message.
  - Response: `{"message": "Hello World"}`

*(API documentation will be available via Swagger UI/ReDoc at `/docs` or `/redoc` once configured in Story 4)*

## Technology Stack

- **Language:** Python 3.9+
- **Framework:** FastAPI
- **Testing:** Pytest
- **Containerization:** Docker

## Contributing

(Placeholder: Guidelines for contributing to this project will be added here.)

## License

(Placeholder: Specify project license, e.g., MIT License.)
