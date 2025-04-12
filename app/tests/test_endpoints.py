from fastapi.testclient import TestClient
from app.main import app # Assuming app is defined in app/main.py

client = TestClient(app)

def test_health_check() -> None:
    """Verify the /health endpoint returns 200 OK and the correct status message."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_hello_world() -> None:
    """Verify the /hw endpoint returns 200 OK and the correct 'Hello World' message."""
    response = client.get("/hw")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
