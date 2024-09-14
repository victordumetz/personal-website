"""Module defining the routers for the resume page."""

from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import BASE_DIR, SECTIONS

templates = Jinja2Templates(directory=Path(BASE_DIR, "templates", "resume"))

router = APIRouter()


@router.get("/resume", response_class=HTMLResponse)
async def get_resume(request: Request) -> HTMLResponse:
    """Get the resume page."""
    return templates.TemplateResponse(
        request=request, name="resume.html", context={"sections": SECTIONS}
    )
