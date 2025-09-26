from fastapi import FastAPI
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

@app.get("/health")
def health_check():
    return {"status": "ok"}