from pydantic import BaseModel
from datetime import datetime

class AlertBase(BaseModel):
    source: str
    message: str
    severity: str

class AlertCreate(AlertBase):
    pass

class AlertResponse(AlertBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True