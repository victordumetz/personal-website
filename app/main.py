"""Module initialising the FastAPI application."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

BASE_DIR = Path(__file__).resolve().parent.parent


templates = Jinja2Templates(directory=Path(BASE_DIR, "templates"))

app = FastAPI()

app.mount(
    "/static", StaticFiles(directory=Path(BASE_DIR, "static")), name="static"
)


@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request) -> HTMLResponse:
    """Get the root page."""
    return templates.TemplateResponse(request=request, name="index.html")
