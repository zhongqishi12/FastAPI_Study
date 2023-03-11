from database import Base
from sqlalchemy import Boolean, Column, Integer, String
from pydantic import BaseModel


class Todo(Base):
    __tablename__ = "t_todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)    
