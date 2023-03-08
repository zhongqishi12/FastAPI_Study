from database import Base
from sqlalchemy import Boolean, Column, Integer, String
from pydantic import BaseModel


class Todos(BaseModel):
    __tablename__ = "t_todos"

    id: int = Column(Integer, primary_key=True, index=True)
    title: str = Column(String)
    description: str = Column(String)
    priority: int = Column(Integer)
    completed: bool = Column(Boolean, default=False)
