from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas

router = APIRouter(prefix="/alerts", tags=["alerts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.AlertResponse)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    new_alert = models.Alert(**alert.dict())
    db.add(new_alert)
    db.commit()
    db.refresh(new_alert)
    return new_alert

@router.get("/", response_model=list[schemas.AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    return db.query(models.Alert).all()