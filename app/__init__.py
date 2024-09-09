"""Package defining the application."""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DATABASE_PATH = Path(BASE_DIR, "database.db")

SECTIONS = [
    {"name": "About", "order": 1, "html_id": "about", "has_page": False},
    {"name": "Skills", "order": 2, "html_id": "skills", "has_page": False},
    {"name": "Projects", "order": 3, "html_id": "projects", "has_page": True},
    {"name": "Contact", "order": 4, "html_id": "contact", "has_page": False},
]
