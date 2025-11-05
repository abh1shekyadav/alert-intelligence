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

@router.post("/{source}/")
def create_alert(source: str, payload: dict, db: Session = Depends(get_db)):
    normalized = normalize_alert(payload, source)
    alert = models.Alert(**normalized)
    db.add(alert)
    db.commit()
    db.refresh(alert)
    return alert

@router.get("/", response_model=list[schemas.AlertResponse])
def get_alerts(db: Session = Depends(get_db)):
    return db.query(models.Alert).all()


def normalize_alert(payload: dict, source: str) -> dict:
    if source == "squadcast":
        return {
             "source": source,
            "source_id": payload.get("id"),
            "message": payload.get("message"),
            "severity": payload.get("severity", "unknown"),
            "raw_payload": payload,
        }
    elif source == "prometheus":
        return {
            "source": source,
            "source_id": payload.get("fingerprint"),
            "message": payload.get("annotations", {}).get("summary", "no message"),
            "severity": payload.get("labels", {}).get("severity", "unknown"),
            "raw_payload": payload,
        }
    else:
        raise ValueError(f"Unsupported alert source: {source}")