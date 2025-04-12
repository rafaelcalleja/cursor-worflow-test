from fastapi.testclient import TestClient
from app.main import app # Assuming app is defined in app/main.py

client = TestClient(app)

def test_health_check():
    """Tests the /health endpoint for status code and response body."""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_hello_world():
    """Tests the /hw endpoint for status code and response body."""
    response = client.get("/hw")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
