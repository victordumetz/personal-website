"""Module defining the routers for the "I like ..." element."""

import itertools
import random
from collections import deque
from collections.abc import Generator
from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app import BASE_DIR

I_LIKE_ITEMS = [
    "judo",
    "bouldering",
    "cooking",
    "linguistics",
    "music",
    "drip coffee",
    "the game of go",
    "(algorithmic) art",
    "seeing plants grow",
]

templates = Jinja2Templates(
    directory=Path(BASE_DIR, "templates", "sections", "partials")
)

router = APIRouter()


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
