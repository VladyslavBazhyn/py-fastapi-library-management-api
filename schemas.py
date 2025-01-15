from datetime import datetime

from pydantic import BaseModel


class AuthorBase(BaseModel):
    name: str
    bio: str


class BookBase(BaseModel):
    title: str
    summary: str
    publication_date: datetime
    author_id: int


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True
