from datetime import datetime, timedelta
from fastapi import Depends, FastAPI
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session
from models import Todo
from schemas import TodoBase, User
from database import SessionLocal
from jose import JWTError, jwt
from typing import Union


app = FastAPI()

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    }
}

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def get_db():
    try:
        db = SessionLocal()
        return db
    finally:
        db.close()


def create_token(user, expires_delta: Union[timedelta, None] = None):
    to_encode = user.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@app.post("/login")
async def user_login(user: User, db: Session = Depends(get_db)):
    user = fake_users_db[user.username]
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    token = create_token(user)
    return {'token':token}
    

@app.get("/todos")
async def get_todos(db: Session = Depends(get_db)):
    return db.query(Todo).all()


@app.get("/todos/{todo_id}")
async def get_todo_by_id(todo_id: int, db: Session = Depends(get_db)):
    return db.query(Todo).filter(Todo.id == todo_id).first()


@app.post("/todos")
async def create_todo(todo: TodoBase, db: Session = Depends(get_db)):
    todo_model = Todo(**todo.dict())
    db.add(todo_model)
    db.commit()
    return {
        'status': 201,
        'message': 'Successful'
    }


@app.put("/todos/{todo_id}")
async def update_todo(todo_id: int, todo: TodoBase, db: Session = Depends(get_db)):
    todo_model = db.query(Todo).filter(Todo.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found')

    todo_data = todo.dict(exclude_unset=True)
    for key, value in todo_data.items():
        setattr(todo_model, key, value)
    db.add(todo_model)
    db.commit()

    return {
        'status': 201,
        'message': 'Update Successful'
    }
