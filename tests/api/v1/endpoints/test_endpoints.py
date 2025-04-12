from fastapi.testclient import TestClient
from app.main import app
from app.models.response import HealthStatus, Message

client = TestClient(app)

def test_health_check():
    """Test the /api/v1/health endpoint."""
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    # Validate response against the Pydantic model
    data = response.json()
    assert HealthStatus(**data) == HealthStatus(status="healthy")

def test_hello_world():
    """Test the /api/v1/hw endpoint."""
    response = client.get("/api/v1/hw")
    assert response.status_code == 200
    # Validate response against the Pydantic model
    data = response.json()
    assert Message(**data) == Message(message="Hello World")
