from sqlalchemy import Column, Integer, String, DateTime, func
from .database import Base

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    message = Column(String)
    severity = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
