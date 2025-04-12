import logging
from fastapi import FastAPI, Request
import time
# Correct the import path for the v1 endpoints router
from app.api.v1.endpoints import endpoints as api_v1_endpoints
# Import the new system endpoint router
from app.api.v1.endpoints import system as api_v1_system

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    """Logs incoming request details and processing time.

    This middleware intercepts every HTTP request. It logs:
    - The method and URL path of the incoming request.
    - The final status code of the response.
    - The total time taken to process the request.

    It does not modify the request or response bodies, nor does it add
    any custom headers.
    """
    start_time = time.time()
    logger.info(f"Incoming request: {request.method} {request.url.path}")
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Request finished: {request.method} {request.url.path} - Status: {response.status_code} - Duration: {process_time:.4f}s")
    return response

# Include the router from the v1 endpoints module with prefix and tags
app.include_router(api_v1_endpoints.router, prefix="/api/v1", tags=["v1"])
# Include the system router
app.include_router(api_v1_system.router, prefix="/api/v1", tags=["system"])
