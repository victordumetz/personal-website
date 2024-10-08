"""Submodule defining the routers for the index page."""

import itertools
import random
from collections import deque
from collections.abc import Awaitable, Callable, Generator
from pathlib import Path
from typing import Literal
from urllib.parse import urlencode

from fastapi import APIRouter, Depends, Form, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app import BASE_DIR, I_LIKE_ITEMS, SECTIONS
from app.crud.message import create_message
from app.crud.projects import get_projects
from app.database import get_db
from app.schemas.message import MessageBase, MessageCreate

EMPTY_MESSAGE = {"name": "", "email": "", "message": ""}
EMPTY_ERROR_CONTEXT = {"name": "", "email": "", "message": ""}
VALID_CLASSES = {"name": "valid", "email": "valid", "message": "valid"}


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


@router.get("/contact-form", response_class=HTMLResponse)
async def get_contact_form(
    request: Request,
    values: dict[Literal["name", "email", "message"], str] | None = None,
    errors: dict[Literal["name", "email", "message"], str] | None = None,
) -> HTMLResponse:
    """Get the contact form."""
    if values is None:
        values = {"name": "", "email": "", "message": ""}
    if errors is None:
        errors = {"name": "", "email": "", "message": ""}

    return templates.TemplateResponse(
        request=request,
        name="contact_form.html",
        context={
            "query_parameters": {
                "name": urlencode(
                    {"name": values["name"], "error": errors["name"]}
                ),
                "email": urlencode(
                    {"email": values["email"], "error": errors["email"]}
                ),
                "message": urlencode(
                    {"message": values["message"], "error": errors["message"]}
                ),
            },
            "success": False,
        },
    )


@router.get("/contact-form/name", response_class=HTMLResponse)
async def get_name_input(
    request: Request, name: str = "", error: str = ""
) -> HTMLResponse:
    """Get the contact form name input."""
    return templates.TemplateResponse(
        request=request,
        name="name_input.html",
        context={"values": {"name": name}, "errors": {"name": error}},
    )


@router.get("/contact-form/email", response_class=HTMLResponse)
async def get_email_input(
    request: Request, email: str = "", error: str = ""
) -> HTMLResponse:
    """Get the contact form email input."""
    return templates.TemplateResponse(
        request=request,
        name="email_input.html",
        context={"values": {"email": email}, "errors": {"email": error}},
    )


@router.get("/contact-form/message", response_class=HTMLResponse)
async def get_message_input(
    request: Request, message: str = "", error: str = ""
) -> HTMLResponse:
    """Get the contact form message input."""
    return templates.TemplateResponse(
        request=request,
        name="message_input.html",
        context={"values": {"message": message}, "errors": {"message": error}},
    )


# Contact form fields validation methods


@router.post("/contact-form/name")
async def validate_name(
    request: Request, name: str = Form("")
) -> HTMLResponse:
    """Validate the name input."""
    try:
        MessageBase.__pydantic_validator__.validate_assignment(
            MessageBase.model_construct(), "name", name
        )

    except ValidationError as errors:
        error_message = ""
        for error in errors.errors():
            if error.get("loc", ())[0] == "name":
                error_message = error["msg"]

        return templates.TemplateResponse(
            request=request,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            name="name_input.html",
            context={
                "values": {"name": name},
                "errors": {"name": error_message},
            },
        )

    return templates.TemplateResponse(
        request=request,
        name="name_input.html",
        context={"values": {"name": name}, "errors": {"name": ""}},
    )


@router.post("/contact-form/email")
async def validate_email(
    request: Request, email: str = Form("")
) -> HTMLResponse:
    """Validate the email input."""
    try:
        MessageBase.__pydantic_validator__.validate_assignment(
            MessageBase.model_construct(), "email", email
        )

    except ValidationError as errors:
        error_message = ""
        for error in errors.errors():
            if error.get("loc", ())[0] == "email":
                error_message = error["msg"]

        return templates.TemplateResponse(
            request=request,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            name="email_input.html",
            context={
                "values": {"email": email},
                "errors": {"email": error_message},
            },
        )

    return templates.TemplateResponse(
        request=request,
        name="email_input.html",
        context={"values": {"email": email}, "errors": {"email": ""}},
    )


@router.post("/contact-form/message")
async def validate_message(
    request: Request, message: str = Form("")
) -> HTMLResponse:
    """Validate the message input."""
    try:
        MessageBase.__pydantic_validator__.validate_assignment(
            MessageBase.model_construct(), "message", message
        )

    except ValidationError as errors:
        error_message = ""
        for error in errors.errors():
            if error.get("loc", ())[0] == "message":
                error_message = error["msg"]

        return templates.TemplateResponse(
            request=request,
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            name="message_input.html",
            context={
                "values": {"message": message},
                "errors": {"message": error_message},
            },
        )

    return templates.TemplateResponse(
        request=request,
        name="message_input.html",
        context={"values": {"message": message}, "errors": {"message": ""}},
    )


# Contact form POST method


@router.post("/contact-form")
async def post_contact_form(
    request: Request,
    name: str = Form(""),
    email: str = Form(""),
    message: str = Form(""),
    db: Session = Depends(get_db),
) -> HTMLResponse:
    """Post the contact form."""
    try:
        validated_message = MessageCreate(
            name=name, email=email, message=message
        )
    except ValidationError as errors:
        error_messages = {"name": "", "email": "", "message": ""}
        for error in errors.errors():
            input_name = str(error["loc"][0])
            error_message = error.get("ctx", {}).get("reason", error["msg"])

            error_messages[input_name] = error_message

        return templates.TemplateResponse(
            request=request,
            name="contact_form.html",
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            context={
                "query_parameters": {
                    "name": urlencode(
                        {
                            "name": name,
                            "error": error_messages["name"],
                        }
                    ),
                    "email": urlencode(
                        {
                            "email": email,
                            "error": error_messages["email"],
                        }
                    ),
                    "message": urlencode(
                        {
                            "message": message,
                            "error": error_messages["message"],
                        }
                    ),
                },
                "success": False,
            },
        )

    create_message(db=db, message=validated_message)

    return templates.TemplateResponse(
        request=request,
        name="contact_form.html",
        status_code=status.HTTP_201_CREATED,
        context={
            "query_parameters": {
                "name": urlencode({"name": "", "error": ""}),
                "email": urlencode({"email": "", "error": ""}),
                "message": urlencode({"message": "", "error": ""}),
            },
            "success": True,
        },
    )
