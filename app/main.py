"""Module initialising the FastAPI application."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from . import BASE_DIR, SECTIONS
from .routers import index, projects, resume

templates = Jinja2Templates(directory=Path(BASE_DIR, "templates", "index"))

app = FastAPI()
app.mount(
    "/static", StaticFiles(directory=Path(BASE_DIR, "static")), name="static"
)
app.include_router(index.router)
app.include_router(projects.router)
app.include_router(resume.router)


@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request) -> HTMLResponse:
    """Get the root page."""
    return templates.TemplateResponse(
        request=request, name="index.html", context={"sections": SECTIONS}
    )
