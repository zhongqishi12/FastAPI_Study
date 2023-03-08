from database import Base
from sqlalchemy import Boolean, Column, Integer, String

class Todos(Base):
    __tablename__ = "t_todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    completed = Column(Boolean, default=False)
