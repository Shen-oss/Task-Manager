from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    username : str
    password : str

class UserRead(BaseModel):
    id : int 
    username : str
    class Config:
        from_attributes = True
    
class TaskCreate(BaseModel):
    title: str
    category: str | None = "life"
    status: str | None = "todo"
    due_date: date | None = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    category: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[date] = None

class TaskRead(BaseModel):
    id : int 
    title: str
    category: str
    status: str
    due_date: date | None = None
    class Config:
        from_attributes = True