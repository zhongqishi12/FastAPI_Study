# This is a sample Python script.
from typing import Union
from enum import Enum
from fastapi import FastAPI

app = FastAPI()


BOOKS = {
    'book_1': {'title': 'Title One', 'author': 'Author One'},
    'book_2': {'title': 'Title Two', 'author': 'Author Two'},
    'book_3': {'title': 'Title Three', 'author': 'Author Three'},
    'book_4': {'title': 'Title Four', 'author': 'Author Four'},
    'book_5': {'title': 'Title Five', 'author': 'Author Five'},
}

class DirectionName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"
    
    
@app.get("/books")
def get_books(skip_book: str = "book_3"):
    new_books = BOOKS.copy()
    del new_books[skip_book]
    return new_books

@app.get("/books/{book_id}")
def get_book(book_id:DirectionName):
    return {"book_title":BOOKS[book_id]}

@app.put("/{book_name}")
async def update_book(book_name: str, book_title: str, book_author: str):
    book_info = {'title':book_title, 'author':book_author}
    BOOKS[book_name] = book_info
    return BOOKS[book_name]
