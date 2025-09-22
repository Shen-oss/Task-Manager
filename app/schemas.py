from pydantic import BaseModel

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

class TaskRead(BaseModel):
    id : int 
    title: str
    completed: bool
    class Config:
        from_attributes = True