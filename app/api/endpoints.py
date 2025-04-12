from fastapi import APIRouter

router = APIRouter()

@router.get("/health", status_code=200)
def health_check():
    """Endpoint to check the service health.

    Returns:
        dict: A dictionary indicating the service status.
    """
    # [RATIONALE] Simple health check for MVP, returns a fixed status.
    return {"status": "healthy"}

@router.get("/hw", status_code=200)
def hello_world():
    """Endpoint that returns a Hello World message.

    Returns:
        dict: A dictionary containing the Hello World message.
    """
    return {"message": "Hello World"}
