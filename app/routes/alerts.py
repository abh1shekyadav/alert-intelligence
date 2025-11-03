from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/alerts")
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    new_alert = models.Alert(**alert.dict())
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert

@router.get("/alerts")
def get_alerts(db: Session = Depends(get_db)):
    alerts = db.query(models.Alert).all()
    return alerts