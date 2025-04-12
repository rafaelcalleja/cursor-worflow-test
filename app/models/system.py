from pydantic import BaseModel
from datetime import datetime

class MemoryInfo(BaseModel):
    total: str
    available: str
    percent_used: float

class DiskInfo(BaseModel):
    total: str
    used: str
    free: str
    percent_used: float

class SystemInfoResponse(BaseModel):
    current_time: datetime
    os_info: str
    cpu_info: str # Simplified for now, e.g., "Model Name, X Cores"
    memory: MemoryInfo
    disk: DiskInfo # For root filesystem '/'
    uptime: str 