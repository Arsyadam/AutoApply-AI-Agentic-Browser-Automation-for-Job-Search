"""Encrypted per-user credential model."""

from sqlalchemy import JSON, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, TimestampMixin, UUIDPrimaryKeyMixin


class UserCredential(UUIDPrimaryKeyMixin, TimestampMixin, Base):
    """Encrypted credential blob for a user/provider/kind tuple."""

    __tablename__ = "user_credentials"
    __table_args__ = (
        UniqueConstraint("user_id", "kind", "provider", name="uq_user_credentials_scope"),
    )

    user_id: Mapped[str] = mapped_column(
        String(32), ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True
    )
    kind: Mapped[str] = mapped_column(String(50), nullable=False)
    provider: Mapped[str] = mapped_column(String(50), nullable=False)
    encrypted_blob: Mapped[dict] = mapped_column(JSON, nullable=False)
