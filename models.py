from sqlalchemy import column , integer , string
from database import Base

class Application(Base):
    __tablename__ = "applications"

    id = column(integer, primary_key=True, index=True)
    company_name = column(string, index=True)
    role = column(string, index=True)
    status = column(string, index=True)
    