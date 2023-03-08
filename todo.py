from typing import Union
from enum import Enum
from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from models import Todos
from database import engine, SessionLocal

app = FastAPI()


def get_db():
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()


@app.get("/todos")
async def get_todos(db: Session = Depends(get_db)):
    return db.query(Todos).all()


@app.post("/todo")
async def post_todos(todo: Todos, db: Session = Depends(get_db)):
    pass
