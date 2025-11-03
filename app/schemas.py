from pydantic import BaseModel
from datetime import datetime

class AlertCreate(BaseModel):
    source: str
    message: str
    severity: str

class AlertRead(AlertCreate):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True