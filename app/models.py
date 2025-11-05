from datetime import datetime
from sqlalchemy import JSON, Column, Integer, String, DateTime, func
from .database import Base

class Alert(Base):
    __tablename__ = "alerts"
    
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    source_id = Column(String, nullable=True)
    message = Column(String)
    severity = Column(String)
    received_at = Column(DateTime, default=datetime.utcnow)
    raw_payload = Column(JSON, nullable=True)
