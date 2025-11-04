from fastapi import FastAPI
from .routes import alerts
from . import models
from .database import engine


models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Alert Intelligence")
app.include_router(alerts.router)


@app.get("/")
def root():
    return {"message": "Alert Intelligence API is running"}