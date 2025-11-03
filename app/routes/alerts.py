from fastapi import APIRouter
from pydantic import BaseModel
from ..database import SessionLocal
from ..models import Alert

router = APIRouter()

class AlertIn(BaseModel):
    source: str
    message: str
    severity: str

@router.post("/alerts")
def create_alert(alert: AlertIn):
    db = SessionLocal()
    new_alert = Alert(**alert.dict())
    db.add(new_alert)
    db.commit()
    return {"status": "ok", "message": "Alert stored"}

@router.get("/alerts")
def get_alerts():
    db = SessionLocal()
    alerts = db.query(Alert).all()
    return alerts