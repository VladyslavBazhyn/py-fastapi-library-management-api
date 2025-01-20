from typing import Union

from fastapi import FastAPI
from sqlalchemy.orm import Session

import crud
import schemas
from database import Base, engine

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/authors/create/", response_model=schemas.Author)
def create_author(db: Session, author: schemas.AuthorCreate):
    return crud.create_author(db, author)


@app.get("/books/create/", response_model=schemas.Book)
def create_book(db: Session, book: schemas.BookCreate):
    return crud.create_book(db, book)


@app.get("/authors/", response_model=list[schemas.Author])
def get_authors(db: Session, skip: int, limit: int):
    return crud.get_authors(db, skip, limit)


@app.get("/authors/{item_id}", response_model=schemas.Author)
def get_author(db: Session, author_id: int):
    return crud.get_author(db, author_id)


@app.get("/books/", response_model=list[schemas.Book])
def get_books(db: Session, skip: int, limit: int):
    return crud.get_books(db, skip, limit)


@app.get("/books/{item_id}", response_model=schemas.Book)
def get_book(db: Session, book_id: int):
    return crud.get_book(db, book_id)
