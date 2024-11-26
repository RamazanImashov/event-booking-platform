from typing import Optional
from sqlalchemy import String, Text, DateTime, Boolean, func, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.helper.database import Base
from uuid import uuid4
from datetime import datetime


class EventModel(Base):
    __tablename__ = "events"

    id: Mapped[UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=lambda: str(uuid4()))
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    start_data: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    end_data: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    location: Mapped[str] = mapped_column(String(255), nullable=False)
    number_of_tickets: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow, nullable=False)
    organizer_id: Mapped[str] = mapped_column(String(255), nullable=False)
    organizer_name: Mapped[str] = mapped_column(String(255), nullable=False)
    organizer_email: Mapped[str] = mapped_column(String(255), nullable=False)

    tags = relationship("TagModel", secondary="event_tags", back_populates="events")



