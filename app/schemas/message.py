"""Submodule defining the message schema."""

from datetime import UTC, datetime
from typing import Annotated

from pydantic import BaseModel, ConfigDict, EmailStr, StringConstraints


class MessageBase(BaseModel):
    """Base schema for a message."""

    name: Annotated[
        str, StringConstraints(strip_whitespace=True, min_length=1)
    ]
    email: EmailStr
    message: Annotated[str, StringConstraints(strip_whitespace=True)]


class MessageCreate(MessageBase):
    """Create schema for a message."""

    sent_datetime: datetime = datetime.now(tz=UTC)


class Message(MessageBase):
    """Message schema."""

    model_config = ConfigDict(from_attributes=True)

    id: int
