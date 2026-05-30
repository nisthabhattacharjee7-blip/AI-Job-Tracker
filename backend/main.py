from fastapi import FastAPI
from backend.schemas import ApplicationCreate
from backend.crud import create_application
from backend.database import SessionLocal, engine
from backend.models import Base, Application

from fastapi import File, UploadFile
import shutil
from backend.ats.parser import extract_text_from_pdf
from backend.ats.scorer import calculate_ats_score

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/applications/")
def create_app(app: ApplicationCreate):

    db = SessionLocal()

    db_app = create_application(db, app)

    db.close()

    return db_app

@app.post("/analyze_resume/")
async def analyze_resume(file: UploadFile = File(...)):
    file_path = f"backend/uploads/{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    resume_text = extract_text_from_pdf(file_path)
    ats_result = calculate_ats_score(resume_text)

    return ats_result