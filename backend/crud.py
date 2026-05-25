from sqlalchemy.orm import Session
from backend.schemas import ApplicationCreate
from backend.models import Application

def create_application(db: Session, app:ApplicationCreate):
    db_app = Application(
        company_name=app.company_name,
        role=app.role,
        status=app.status
    )

    db.add(db_app)
    db.commit()
    db.refresh(db_app)

    return db_app
