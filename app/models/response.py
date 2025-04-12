from pydantic import BaseModel

class HealthStatus(BaseModel):
    status: str

class Message(BaseModel):
    message: str 