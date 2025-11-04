from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./alerts.db"

DATABASE_URL = "postgresql://username:password@localhost/alertdb"

engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False } if DATABASE_URL.startswith("sqlite") else {}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()