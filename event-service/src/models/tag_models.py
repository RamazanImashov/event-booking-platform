from sqlalchemy import String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.helper.database import Base
from uuid import uuid4
from datetime import datetime
from .event_models import EventModel


class TagModel(Base):
    __tablename__ = "tags"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)

    events = relationship("EventModel", secondary="event_tags", back_populates="tags")


class EventTagAssociation(Base):
    __tablename__ = "event_tags"

    event_id: Mapped[UUID] = mapped_column(ForeignKey("events.id", ondelete="CASCADE"), primary_key=True)
    tag_id: Mapped[UUID] = mapped_column(ForeignKey("tags.id", ondelete="CASCADE"), primary_key=True)
