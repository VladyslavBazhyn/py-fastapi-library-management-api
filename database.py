import sqlalchemy

from fastapi import FastAPI


app = FastAPI()

DATABASE_URL = "sqlite:///./library.db"

engine = sqlalchemy.create_engine(DATABASE_URL)

SessionLocal = sqlalchemy.orm.sessionmaker(
    autocommit=False, autoflush=False, bind=engine
)

Base = sqlalchemy.ext.declarative.declarative_base()


def get_db():
    db = sqlalchemy.orm.Sessionmaker()
    try:
        yield db
    finally:
        db.close()
