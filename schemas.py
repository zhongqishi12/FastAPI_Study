from pydantic import BaseModel


class TodoBase(BaseModel):
    title: str
    description: str
    priority: int
    completed: bool
    
class User(BaseModel):
    username: str
    password: str
