from typing import Union
from fastapi import FastAPI,HTTPException, Header
from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID

app = FastAPI()

class Book(BaseModel):
    id: UUID
    title: str = Field(min_length=2)
    author: str
    description: Optional[str]
    rating: str
    
    class Config:
        schema_extra = {
            'example':{
                'id':"11111",
                'title':'Book title'
            }
        }
    
BOOKS = []

@app.get("/")
async def get_all_books():
    return BOOKS

@app.post("/")
async def create_book(book: Book):
    BOOKS.append(book)
    return BOOKS

@app.delete("/{book_id}")
async def delete_book(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    raise HTTPException(404,'Book Not found')
    
@app.get("/book{book_id}")
async def read_book(book_id:UUID):
    for x in BOOKS:
        if x.id == book_id:
            return x
    
    
@app.get('/header')
async def get_header(user_agent: Union[str, None] = Header(default=None)):
    print(user_agent)
    return {"User-Agent": user_agent}


@app.get('/books/login')
async def book_login(book_id: UUID, username: Union[str, None] = Header(default=None), password: Union[str, None] = Header(default=None)):
    if (username == 'FastAPIUser' and password == 'test1234'):
        return BOOKS[book_id]
    return HTTPException(401,'Invalid username or password')
    