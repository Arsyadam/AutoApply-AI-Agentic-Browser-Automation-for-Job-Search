"""Per-user LLM provider configuration model."""

from sqlalchemy import JSON, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class UserLLMConfig(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Stores a user's preferred LLM provider settings."""

    __tablename__ = "user_llm_configs"

    user_id: Mapped[str] = mapped_column(
        String(32), ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False, index=True
    )
    preferred_provider: Mapped[str | None] = mapped_column(String(50), nullable=True)
    fallback_providers: Mapped[list] = mapped_column(JSON, nullable=False, default=list)
    model_overrides: Mapped[dict] = mapped_column(JSON, nullable=False, default=dict)
