"""Module initialising the FastAPI application."""

from pathlib import Path

from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory=Path("templates"))

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def get_root(request: Request) -> HTMLResponse:
    """Get the root page."""
    return templates.TemplateResponse(request=request, name="index.html")
