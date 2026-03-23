import uuid
from datetime import datetime
from sqlalchemy import String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base, TimestampMixin

class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    agent_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("agents.id", ondelete="CASCADE"),
        nullable=False,
    )
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    is_auto: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    next_run: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,      # None = chưa schedule hoặc task manual
    )
    is_manual: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    force_action: Mapped[bool | None] = mapped_column(
        String(20),
        nullable=True,      # "start" | "stop" | "approve" | None
    )

    agent: Mapped["Agent"] = relationship("Agent", back_populates="tasks")
    job: Mapped["Job"] = relationship(
        "Job",
        back_populates="task",
        cascade="all, delete-orphan",
    )