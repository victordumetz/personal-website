"""Submodule defining the routers for the index page."""

import itertools
import random
from collections import deque
from collections.abc import Awaitable, Callable, Generator
from pathlib import Path

from fastapi import APIRouter, Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app import BASE_DIR, I_LIKE_ITEMS, SECTIONS
from app.crud.projects import get_projects
from app.database import get_db

common_templates = Jinja2Templates(
    directory=Path(BASE_DIR, "templates", "common")
)
templates = Jinja2Templates(
    directory=Path(BASE_DIR, "templates", "index", "partials")
)

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


# TODO: Optimise the refreshing by appending only the next item and
# removing the first one.


def window_generator(
    items: list[str], window_length: int
) -> Generator[list[str | None], None, None]:
    """Yield a sliding window of specified length.

    Parameters
    ----------
    items : list[str]
        List of items to iterate through.
    window_length : int
        Length of the sliding window.

    Yields
    ------
    list[str]
        The sliding window.
    """
    iterator = itertools.cycle(items)
    window = deque(
        (next(iterator, None) for _ in range(window_length)),
        maxlen=window_length,
    )
    for e in iterator:
        window.append(e)
        yield list(window)


i_like_items_generator = window_generator(
    random.sample(I_LIKE_ITEMS, len(I_LIKE_ITEMS)), 7
)


@router.get("/i-like-items", response_class=HTMLResponse)
async def get_i_like_items(request: Request) -> HTMLResponse:
    """Get the "I like" items."""
    return templates.TemplateResponse(
        request=request,
        name="i_like_items.html",
        context={"items": next(i_like_items_generator)},
    )


@router.get("/projects-preview-list", response_class=HTMLResponse)
async def get_projects_preview_list(
    request: Request, db: Session = Depends(get_db)
) -> HTMLResponse:
    """Get the list of projects to display in the "Projects" section."""
    projects = get_projects(db, 0, 3)
    return common_templates.TemplateResponse(
        request=request,
        name="projects_list.html",
        context={"projects": projects},
    )
