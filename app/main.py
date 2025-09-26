from fastapi import FastAPI
from app.db import Base, engine
from app.auth import router as auth_router
from app.tasks import router as tasks_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Manager API")

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])

@app.get("/health")
def health_check():
    return {"status": "ok"}