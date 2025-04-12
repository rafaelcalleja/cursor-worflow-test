from fastapi import APIRouter

from app.models.system import SystemInfoResponse
from app.core.system_utils import get_system_info

router = APIRouter()

@router.get("/system_info", response_model=SystemInfoResponse)
async def read_system_info():
    """
    Retrieve basic system information about the server node.

    Returns information such as OS details, CPU, memory usage,
    disk usage (for root partition), current time, and uptime.
    Requires the process to have permission to read system details
    (typically works for non-root users for basic info via psutil).
    """
    system_info = get_system_info()
    return system_info 