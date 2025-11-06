from sqlalchemy import Column, Integer, String, DateTime, JSON, func
from app.database import Base

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, nullable=False)
    source_id = Column(String, nullable=True)
    message = Column(String, nullable=False)
    severity = Column(String, nullable=False)
    received_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    raw_payload = Column(JSON, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)