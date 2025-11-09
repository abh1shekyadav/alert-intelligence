from sqlalchemy.orm import Session
from app import models, models_enriched, schemas
from datetime import datetime

from app.enrichment import enrich_alert

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

def enrich_and_store_alert(db: Session, alert: models.Alert):
    enriched_data = enrich_alert({
        "id": alert.id,
        "message": alert.message,
        "severity": alert.severity,
        "source": alert.source
    })

    enriched_alert = models_enriched.EnrichedAlert(
        alert_id=alert.id,
        service_owner=enriched_data["service_owner"],
        category=enriched_data["category"],
        severity_weight=enriched_data["severity_weight"],
        tags=enriched_data["tags"]
    )
    db.add(enriched_alert)
    db.commit()
    db.refresh(enriched_alert)
    return enriched_alert