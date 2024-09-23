"""Module defining the routers for the projects page."""

from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app import BASE_DIR, SECTIONS
from app.crud.projects import get_projects
from app.database import get_db

common_templates = Jinja2Templates(
    directory=Path(BASE_DIR, "templates", "common")
)
templates = Jinja2Templates(directory=Path(BASE_DIR, "templates", "projects"))

router = APIRouter()


@router.get("/projects", response_class=HTMLResponse)
async def get_projects_page(request: Request) -> HTMLResponse:
    """Get the projects page."""
    return templates.TemplateResponse(
        request=request, name="projects.html", context={"sections": SECTIONS}
    )


@router.get("/projects-list", response_class=HTMLResponse)
async def get_all_projects_list(
    request: Request, db: Session = Depends(get_db)
) -> HTMLResponse:
    """Get the list of projects to display in the "Projects" section."""
    projects = get_projects(db)
    return common_templates.TemplateResponse(
        request=request,
        name="projects_list.html",
        context={"projects": projects},
    )
