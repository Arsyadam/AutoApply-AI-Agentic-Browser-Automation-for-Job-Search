"""Authentication request and response schemas."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class RegisterRequest(BaseModel):
    """Registration payload."""

    email: EmailStr
    password: str = Field(min_length=8)
    full_name: str | None = None


class TokenResponse(BaseModel):
    """Access token response."""

    access_token: str
    token_type: str = "bearer"


class UserResponse(BaseModel):
    """Public user profile payload."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    email: EmailStr
    full_name: str | None = None
    is_active: bool = True
    is_superuser: bool = False
    created_at: datetime | None = None
    updated_at: datetime | None = None


class WSTicketResponse(BaseModel):
    """Short-lived websocket ticket response."""

    ticket: str
