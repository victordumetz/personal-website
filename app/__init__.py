"""Package defining the application."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = Path(BASE_DIR, "database.db")
