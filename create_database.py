"""Create the database."""

import sqlite3

from app import DATABASE_PATH

# create the database if it doesn't exist
if not DATABASE_PATH.is_file():
    conn = None
    try:
        conn = sqlite3.connect(DATABASE_PATH)
    finally:
        if conn is not None:
            conn.close()
