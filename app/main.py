from fastapi import FastAPI
from app.routes import alerts
from app.database import Base, engine

app = FastAPI(title="Alert Intelligence")

Base.metadata.create_all(bind=engine)
app.include_router(alerts.router)


@app.get("/")
def root():
    return {"message": "Alert Intelligence API is running"}