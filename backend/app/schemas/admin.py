"""Admin response schemas."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, ConfigDict


class SystemIssueResponse(BaseModel):
    """Serialized system-issue row for admin endpoints."""

    model_config = ConfigDict(from_attributes=True)

    id: str
    user_id: str | None = None
    category: str
    severity: str
    signals: dict[str, Any]
    diagnosis: str
    status: str
    detected_at: datetime
    created_at: datetime | None = None
    updated_at: datetime | None = None
