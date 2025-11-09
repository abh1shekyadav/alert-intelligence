from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/alerts", tags=["alerts"])

# Dependency to get a DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.AlertResponse)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    return crud.create_alert(db=db, alert=alert)


@router.get("/", response_model=schemas.PaginatedAlerts)
def get_alerts(
    skip: int = Query(0, ge=0, description="Pagination start index"),
    limit: int = Query(10, ge=1, le=100, description="Number of alerts to fetch"),
    db: Session = Depends(get_db)
):
    total, alerts = crud.get_alerts(db=db, skip=skip, limit=limit)
    return {"total": total, "items": alerts}


@router.get("/{alert_id}", response_model=schemas.AlertResponse)
def get_alert(alert_id: int, db: Session = Depends(get_db)):
    alert = crud.get_alert(db=db, alert_id=alert_id)
    if not alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return alert

@router.post("/", response_model=schemas.AlertResponse)
def create_alert(alert: schemas.AlertCreate, db: Session = Depends(get_db)):
    new_alert = crud.create_alert(db=db, alert=alert)
    # Trigger enrichment pipeline
    crud.enrich_and_store_alert(db, new_alert)
    return new_alert