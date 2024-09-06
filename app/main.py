"""Module initialising the FastAPI application."""

from pathlib import Path

from fastapi import Depends, FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from . import BASE_DIR, crud, models
from .database import engine, get_db
from .routers import sections

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates(directory=Path(BASE_DIR, "templates"))

app = FastAPI()
app.mount(
    "/static", StaticFiles(directory=Path(BASE_DIR, "static")), name="static"
)
app.include_router(sections.router)


@app.get("/", response_class=HTMLResponse)
async def get_root(
    request: Request, db: Session = Depends(get_db)
) -> HTMLResponse:
    """Get the root page."""
    sections = crud.get_sections(db)

    return templates.TemplateResponse(
        request=request, name="index.html", context={"sections": sections}
    )
