from pydantic import BaseModel

class ApplicationCreate(BaseModel):
    company_name: str
    role: str
    status: str
        
