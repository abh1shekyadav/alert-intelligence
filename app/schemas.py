from pydantic import BaseModel
from datetime import datetime
from typing import Optional, Any, List

class AlertBase(BaseModel):
    source: str
    source_id: Optional[str] = None
    message: str
    severity: str

class AlertCreate(AlertBase):
    raw_payload: Optional[Any] = None

class AlertResponse(AlertBase):
    id: int
    received_at: datetime
    created_at: datetime

    class Config:
        orm_mode = True

class PaginatedAlerts(BaseModel):
    total: int
    items: List[AlertResponse]