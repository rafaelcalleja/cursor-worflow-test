from fastapi import APIRouter
from app.models.response import HealthStatus, Message

router = APIRouter()

@router.get("/health", status_code=200, response_model=HealthStatus)
def health_check() -> HealthStatus:
    """Endpoint to check the service health.

    Returns:
        HealthStatus: An object indicating the service status.
    """
    # [RATIONALE] Simple health check for MVP, returns a fixed status.
    return HealthStatus(status="healthy")

@router.get("/hw", status_code=200, response_model=Message)
def hello_world() -> Message:
    """Endpoint that returns a Hello World message.

    Returns:
        Message: An object containing the Hello World message.
    """
    return Message(message="Hello World")
