from fastapi import FastAPI
from app.routes import alerts
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Alert Intelligence")

app.include_router(alerts.router)

@app.get("/")
def root():
    return {"message": "Alert Intelligence API is running"}