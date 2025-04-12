from fastapi import APIRouter

router = APIRouter()

@router.get("/health", status_code=200)
def health_check():
    """Endpoint to check the service health.

    Returns:
        dict: A dictionary indicating the service status.
    """
    # Simple health check, returns a fixed status
    return {"status": "healthy"}
