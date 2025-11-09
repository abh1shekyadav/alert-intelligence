from sqlalchemy import JSON, Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship
from app.database import Base


class EnrichedAlert(Base):
    __tablename__ = "enriched_alerts"

    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer, ForeignKey("alerts.id", ondelete="CASCADE"), nullable=False)
    service_owner = Column(String, nullable=True)
    category = Column(String, nullable=True)
    severity_weight = Column(Integer, nullable=True)
    tags = Column(JSON, nullable=True)
    enriched_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    alert = relationship("Alert", backref="enriched_record")