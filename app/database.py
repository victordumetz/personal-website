"""Module defining database related tools."""

import sqlite3
from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from . import DATABASE_PATH

# create the database if it doesn't exist
if not DATABASE_PATH.is_file():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
    finally:
        if conn is not None:
            conn.close()

engine = create_engine(
    f"sqlite:///{DATABASE_PATH!s}", connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db() -> Generator:
    """Get the database."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
