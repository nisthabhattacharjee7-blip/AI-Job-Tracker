from fastapi import FastAPI
from schemas import ApplicationCreate
from crud import create_application
from database import SessionLocal, engine
from models import Base, Application

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/applications/")
def create_app(app: ApplicationCreate):

    db = SessionLocal()

    db_app = create_application(db, app)

    db.close()

    return db_app
