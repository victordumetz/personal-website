"""Submodule defining the routers for the "About" section."""

from collections.abc import Awaitable, Callable
from pathlib import Path

from fastapi import APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import BASE_DIR, SECTIONS

templates = Jinja2Templates(directory=Path(BASE_DIR, "templates", "sections"))

router = APIRouter()


def create_section_endpoint(
    section: str,
) -> Callable[[Request], Awaitable[HTMLResponse]]:
    """Create the endpoint for the given section."""

    async def get_section(request: Request) -> HTMLResponse:
        """Get the section's section."""
        return templates.TemplateResponse(
            request=request, name=f"{section}_section.html"
        )

    get_section.__name__ = f"get_{section}_section"

    return get_section


for section in SECTIONS:
    router.add_api_route(
        f"/{section["html_id"]}-section",
        create_section_endpoint(section["html_id"]),
        methods=["GET"],
        response_class=HTMLResponse,
    )
