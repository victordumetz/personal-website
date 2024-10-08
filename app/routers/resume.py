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
from app.crud.language import get_formatted_languages
from app.crud.professional_experience import (
    get_formatted_professional_experiences,
)
from app.crud.school_attendance import get_formatted_school_attendances
from app.database import get_db
from app.schemas.language import FormattedLanguage
from app.schemas.professional_experience import FormattedProfessionalExperience
from app.schemas.school_attendance import FormattedSchoolAttendance

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


@router.get(
    "/education",
    response_model=list[FormattedSchoolAttendance],
    response_class=HTMLResponse,
)
async def get_education(
    request: Request,
    hx_request: Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db),
) -> HTMLResponse | JSONResponse:
    """Get the education section."""
    education = get_formatted_school_attendances(db)

    if not hx_request:
        return JSONResponse(jsonable_encoder(education))

    education = [
        FormattedSchoolAttendance(
            school_name=school_attendance.name,
            location=school_attendance.location,
            content=school_attendance.content,
            year_month_from=school_attendance.date_from.strftime("%b %Y"),
            year_month_to=school_attendance.date_to.strftime("%b %Y"),
        )
        for school_attendance in education
    ]

    return templates.TemplateResponse(
        request=request,
        name="partials/education.html",
        context={"education": education},
    )


@router.get(
    "/languages",
    response_model=list[FormattedLanguage],
    response_class=HTMLResponse,
)
async def get_languages(
    request: Request,
    hx_request: Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db),
) -> HTMLResponse | JSONResponse:
    """Get the languages section."""
    languages = get_formatted_languages(db)

    if not hx_request:
        return JSONResponse(jsonable_encoder(languages))

    languages = [
        FormattedLanguage(
            name=language.name,
            level=language.level,
            cefr_level=language.cefr_level,
        )
        for language in languages
    ]

    return templates.TemplateResponse(
        request=request,
        name="partials/languages.html",
        context={"languages": languages},
    )


@router.get("/certifications", response_class=HTMLResponse)
async def get_certifications(request: Request) -> HTMLResponse:
    """Get the certifications section."""
    return templates.TemplateResponse(
        request=request, name="partials/certifications.html"
    )


@router.get("/others", response_class=HTMLResponse)
async def get_others(request: Request) -> HTMLResponse:
    """Get the certifications section."""
    return templates.TemplateResponse(
        request=request, name="partials/others.html"
    )
