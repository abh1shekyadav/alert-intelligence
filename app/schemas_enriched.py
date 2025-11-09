import datetime
from typing import Any, List, Optional
from pydantic import BaseModel


class EnrichedAlertBase(BaseModel):
    alert_id: int
    service_owner: Optional[str] = None
    category: Optional[str] = None
    severity_weight: Optional[int] = None
    tags: Optional[Any] = None

class EnrichedAlertResponse(EnrichedAlertBase):
    id: int
    enriched_at: datetime

    class Config:
        orm_mode = True

class PaginatedEnrichedAlerts(BaseModel):
    total: int
    items: List[EnrichedAlertResponse]

    