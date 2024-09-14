"""Module defining the routers for the resume page."""

import json
from pathlib import Path
from typing import Annotated

from fastapi import APIRouter, Depends, Header, Request
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app import BASE_DIR, SECTIONS
from app.crud.professional_experience import (
    get_formatted_professional_experiences,
)
from app.database import get_db
from app.schemas.professional_experience import FormattedProfessionalExperience

templates = Jinja2Templates(directory=Path(BASE_DIR, "templates", "resume"))

router = APIRouter()


@router.get("/resume", response_class=HTMLResponse)
async def get_resume(request: Request) -> HTMLResponse:
    """Get the resume page."""
    return templates.TemplateResponse(
        request=request, name="resume.html", context={"sections": SECTIONS}
    )


@router.get(
    "/professional-experiences",
    response_model=list[FormattedProfessionalExperience],
    response_class=HTMLResponse,
)
async def get_professional_experiences(
    request: Request,
    hx_request: Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db),
) -> HTMLResponse | JSONResponse:
    """Get the professional experiences section."""
    experiences = get_formatted_professional_experiences(db)

    if not hx_request:
        return JSONResponse(jsonable_encoder(experiences))

    experiences = [
        FormattedProfessionalExperience(
            company_name=experience.name,
            location=experience.location,
            job_title=experience.job_title,
            year_month_from=experience.date_from.strftime("%b %Y"),
            year_month_to=experience.date_to.strftime("%b %Y"),
            responsibilities=json.loads(experience.responsibilities),
        )
        for experience in experiences
    ]

    return templates.TemplateResponse(
        request=request,
        name="partials/professional-experiences.html",
        context={"experiences": experiences},
    )
