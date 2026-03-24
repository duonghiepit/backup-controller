import uuid
from datetime import datetime
from sqlalchemy import String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID
from app.models.base import Base, TimestampMixin

class JobStatus():
    RUNNING = "running"
    DONE = "done"
    FAIL = "fail"

class Job(Base, TimestampMixin):
    __tablename__ = "jobs"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )
    task_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("tasks.id", ondelete="CASCADE"),
        nullable=False,
    )
    status: Mapped[str] = mapped_column(
        String(20),
        default=JobStatus.RUNNING,
        nullable=False,
    )
    percentage: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    last_touch: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,     # Update mỗi lần agent report tiến độ
    )
    force_action: Mapped[bool | None] = mapped_column(
        String(20),
        nullable=True,      # "start" | "stop" | "approve" | None
    )

    task: Mapped["Task"] = relationship("Task", back_populates="job")
