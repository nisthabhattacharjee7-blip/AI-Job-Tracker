from fastapi import FastAPI
from backend.schemas import ApplicationCreate
from backend.crud import create_application
from backend.database import SessionLocal, engine
from backend.models import Base, Application

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/applications/")
def create_app(app: ApplicationCreate):

    db = SessionLocal()

    db_app = create_application(db, app)

    db.close()

    return db_app
