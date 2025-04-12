# API Documentation

## 1. Introduction

*Brief overview of the API, its purpose, and intended audience.*

## 2. Getting Started

### 2.1. Prerequisites

*List any software or tools required to use the API (e.g., `curl`, Postman, Python version).*

### 2.2. Local Setup

*Instructions on how to set up and run the project locally. Reference `README.md` if applicable.*

*Example:*
```bash
# Clone the repository
git clone <repository_url>
cd <project_directory>

# Set up virtual environment (Recommended)
python -m venv venv
source venv/bin/activate # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the API server
make run # Or uvicorn app.main:app --reload
```

### 2.3. Base URL

*The base URL for all API endpoints.*

- **Local:** `http://localhost:8000/api/v1`
- **Staging:** *(if applicable)*
- **Production:** *(if applicable)*

## 3. Authentication

*Details about the authentication mechanism (if any). For now, this can state that authentication is not required.*

## 4. Endpoint Reference

*Detailed description of each available endpoint.*

### 4.1. Health Check

*   **Endpoint:** `GET /health`
*   **Description:** Checks the operational status of the API.
*   **Request:**
    *   Method: `GET`
    *   Headers: None
    *   Body: None
*   **Response:**
    *   `200 OK`: API is healthy.
        ```json
        {
          "status": "ok"
        }
        ```
*   **Example (`curl`):**
    ```bash
    curl http://localhost:8000/api/v1/health
    ```

### 4.2. Hello World

*   **Endpoint:** `GET /hw`
*   **Description:** Returns a simple "Hello World" message.
*   **Request:**
    *   Method: `GET`
    *   Headers: None
    *   Body: None
*   **Response:**
    *   `200 OK`: Success.
        ```json
        {
          "message": "Hello World"
        }
        ```
*   **Example (`curl`):**
    ```bash
    curl http://localhost:8000/api/v1/hw
    ```

### 4.3. System Information

*   **Endpoint:** `GET /system_info`
*   **Description:** Retrieves basic system information about the server node where the API is running. This includes OS details, CPU info, memory usage, disk usage (for the root filesystem `/`), current server time, and system uptime. Access is limited to information readable by the process user (non-root assumed).
*   **Request:**
    *   Method: `GET`
    *   Headers: None
    *   Body: None
*   **Response:**
    *   `200 OK`: System information retrieved successfully.
        ```json
        {
          "current_time": "2023-10-27T10:30:00.123456", // ISO 8601 Format
          "os_info": "Linux 5.15.0-generic (Example Version String)",
          "cpu_info": "Intel(R) Core(TM) i7-8700K CPU @ 3.70GHz (12 Cores @ 3700.00Mhz)",
          "memory": {
            "total": "15.50GB",
            "available": "7.80GB",
            "percent_used": 49.7
          },
          "disk": {
            "total": "99.50GB",
            "used": "45.20GB",
            "free": "54.30GB",
            "percent_used": 45.4
          },
          "uptime": "1 days, 02:30:05"
        }
        ```
    *   *(Note: Specific values will vary based on the server environment.)*
*   **Example (`curl`):**
    ```bash
    curl http://localhost:8000/api/v1/system_info
    ```

## 5. Data Models

*Descriptions of the data structures used in requests and responses.*

### 5.1. `HealthStatus`

*   **File:** `app/models/response.py`
*   **Description:** Represents the health status of the API.
*   **Fields:**
    *   `status` (string, required): The status message (e.g., "ok").

### 5.2. `Message`

*   **File:** `app/models/response.py`
*   **Description:** Represents a generic message response.
*   **Fields:**
    *   `message` (string, required): The content of the message.

### 5.3. `MemoryInfo`

*   **File:** `app/models/system.py`
*   **Description:** Represents memory usage information.
*   **Fields:**
    *   `total` (string): Total physical memory (scaled, e.g., "15.50GB").
    *   `available` (string): Available memory (scaled, e.g., "7.80GB").
    *   `percent_used` (float): Percentage of memory used.

### 5.4. `DiskInfo`

*   **File:** `app/models/system.py`
*   **Description:** Represents disk usage information for a specific partition (typically root `/`).
*   **Fields:**
    *   `total` (string): Total disk space (scaled).
    *   `used` (string): Used disk space (scaled).
    *   `free` (string): Free disk space (scaled).
    *   `percent_used` (float): Percentage of disk space used.

### 5.5. `SystemInfoResponse`

*   **File:** `app/models/system.py`
*   **Description:** The response model for the `/system_info` endpoint.
*   **Fields:**
    *   `current_time` (datetime): The current server time (ISO 8601 format).
    *   `os_info` (string): Operating system details.
    *   `cpu_info` (string): CPU model, core count, and frequency.
    *   `memory` (`MemoryInfo`): Memory usage details.
    *   `disk` (`DiskInfo`): Disk usage details for the root partition.
    *   `uptime` (string): System uptime formatted as days, HH:MM:SS.

## 6. Usage Examples

*More comprehensive examples or links to collections.*

### 6.1. Postman Collection

A Postman collection is available for easier testing: [docs/api_collection.postman_collection.json](docs/api_collection.postman_collection.json)

*(Include instructions on how to import and use if needed)*

## 7. Error Handling

*Details on common HTTP status codes and error response formats.*

*   `404 Not Found`: Endpoint does not exist.
*   `422 Unprocessable Entity`: Request validation failed (e.g., invalid parameters).
*   `500 Internal Server Error`: Unexpected server error.

*(Add specific error response structures if defined)*

## 8. Versioning

*Strategy for API versioning (e.g., URI versioning like `/api/v1`).*

Current Version: `v1`

## 9. Contributing

*Guidelines for contributing to the API development (if applicable).*

## 10. Support

*Contact information or channels for getting help.* 