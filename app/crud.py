from sqlalchemy.orm import Session
from app import models, schemas
from datetime import datetime

def create_alert(db: Session, alert: schemas.AlertCreate):
    db_alert = models.Alert(
        source=alert.source,
        source_id=alert.source_id,
        message=alert.message,
        severity=alert.severity,
        received_at=datetime.utcnow(),
        raw_payload=alert.raw_payload
    )
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

def get_alert(db: Session, alert_id: int):
    return db.query(models.Alert).filter(models.Alert.id == alert_id).first()

def get_alerts(db: Session, skip: int = 0, limit: int = 10):
    total = db.query(models.Alert).count()
    alerts = db.query(models.Alert).offset(skip).limit(limit).all()
    return total, alerts