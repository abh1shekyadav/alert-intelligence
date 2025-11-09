from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app import models_enriched, schemas_enriched
from app.database import SessionLocal


router = APIRouter(prefix="/enriched-alerts", tags=["enriched_alerts"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=schemas_enriched.PaginatedEnrichedAlerts)
def get_enriched_alerts(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db)
):
    total = db.query(models_enriched.EnrichedAlert).count()
    alerts = db.query(models_enriched.EnrichedAlert).offset(skip).limit(limit).all()
    return {"total": total, "items": alerts}