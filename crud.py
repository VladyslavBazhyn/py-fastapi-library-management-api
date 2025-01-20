from fastapi import HTTPException
from sqlalchemy.orm import Session

import models, schemas


def get_books(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Book).offset(skip).limit(limit).all()


def get_authors(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Author).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    book = db.query(models.Book).get(book_id, None)

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return book


def get_author(db: Session, author_id: int):
    author = db.query(models.Author).get(author_id, None)

    if author is None:
        raise HTTPException(status_code=404, detail="Book not found")

    return author


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        summary=book.summary,
        publication_date=book.publication_date,
        author_id=book.author_id
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    return db_book


def create_author(db: Session, author: schemas.AuthorCreate):
    db_author = models.Author(
        name=author.name,
        bio=author.bio,
    )

    db.add(db_author)
    db.commit()
    db.refresh(db_author)

    return db_author


def update_book(db: Session, book_id: int, updated_book: schemas.BookCreate):
    db_book = get_book(db=db, book_id=book_id)

    db_book.title = updated_book.title
    db_book.author_id = updated_book.author_id
    db_book.summary = updated_book.summary
    db_book.publication_date = updated_book.publication_date

    db.commit()
    db.refresh(db_book)

    return db_book


def update_author(db: Session, author_id: int, updated_author: schemas.AuthorCreate):
    db_author = get_author(db=db, author_id=author_id)

    db_author.title = updated_author.title
    db_author.author_id = updated_author.author_id
    db_author.summary = updated_author.summary
    db_author.publication_date = updated_author.publication_date

    db.commit()
    db.refresh(db_author)

    return db_author


def delete_book(db: Session, book_id: int):
    db_book = get_book(db=db, book_id=book_id)

    db.delete(db_book)
    db.commit()

    return {"detail": f"Book with id {book_id} has been deleted"}


def delete_author(db: Session, author_id: int):
    db_author = get_author(db=db, author_id=author_id)

    db.delete(db_author)
    db.commit()

    return {"detail": f"Author with id {author_id} has been deleted"}
