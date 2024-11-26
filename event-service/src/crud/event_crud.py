
from typing import Sequence

from uuid import UUID

from fastapi import HTTPException, Request

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload


from ..models.event_models import EventModel

from src.schemas.event_schemas import (
    EventCreateSchema,
    EventResponseSchema,
    EventUpdateSchema,
    EventUpdateSchemaP
)

from src.models.tag_models import TagModel, EventTagAssociation

from datetime import datetime


async def get_all_events_crud(
        session: AsyncSession
) -> Sequence[EventModel]:
    stmt = (
        select(EventModel)
        .options(joinedload(EventModel.tags))
        .order_by(EventModel.created_at)
    )

    result = await session.execute(stmt)
    events = result.unique().scalars().all()

    event_list = []
    for event in events:
        event_dict = event.__dict__
        event_dict['tags'] = [tag.name for tag in event.tags]
        event_list.append(event_dict)

    return event_list


async def get_id_event_crud(
        event_id: UUID,
        session: AsyncSession
) -> EventModel:
    stmt = (
        select(EventModel)
        .options(joinedload(EventModel.tags))
        .where(EventModel.id == event_id)
    )
    result = await session.execute(stmt)
    event = result.scalars().first()

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    # Extract the tag names as a list of strings
    event_tags = [tag.name for tag in event.tags]

    # Assuming that your response model (e.g., EventResponse) accepts tags as a list of strings
    return {
        "id": event.id,
        "title": event.title,
        "description": event.description,
        "start_data": event.start_data,
        "end_data": event.end_data,
        "location": event.location,
        "is_active": event.is_active,
        "number_of_tickets": event.number_of_tickets,
        "organizer_name": event.organizer_name,
        "organizer_email": event.organizer_email,
        "tags": event_tags
    }


def make_naive(dt: datetime) -> datetime:
    if dt.tzinfo is not None:
        return dt.astimezone(None).replace(tzinfo=None)
    return dt


async def create_event_crud(
        session: AsyncSession,
        event_create_schema: EventCreateSchema
) -> EventModel:

    event_data = event_create_schema.model_dump(exclude={"tags"})

    event_data["start_data"] = make_naive(event_data["start_data"])
    event_data["end_data"] = make_naive(event_data["end_data"])

    tags = []
    if event_create_schema.tags:
        stmt = select(TagModel).where(TagModel.id.in_(event_create_schema.tags))
        tags = (await session.scalars(stmt)).all()

    event = EventModel(**event_data)
    event.tags.extend(tags)
    session.add(event)
    await session.commit()
    await session.refresh(event)
    return event


async def update_event_crud(
        event_id: UUID,
        session: AsyncSession,
        event_update_schema: EventUpdateSchema,
        partial: bool = False,
) -> EventModel:
    stmt = (
        select(EventModel)
        .options(joinedload(EventModel.tags))
        .where(EventModel.id == event_id)
    )
    result = await session.execute(stmt)
    event = result.scalars().first()

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    update_data = event_update_schema.model_dump(exclude_unset=partial)

    for key, value in update_data.items():
        if key == "tags" and isinstance(value, list):
            related_tags = await session.execute(
                select(TagModel).where(TagModel.id.in_(value))
            )
            setattr(event, key, related_tags.scalars().all())
        elif isinstance(value, datetime):
            setattr(event, key, make_naive(value))
        else:
            setattr(event, key, value)

    await session.commit()
    await session.refresh(event)
    return event


async def partial_update_event_crud(
        event_id: UUID,
        session: AsyncSession,
        event_update_schema: EventUpdateSchema,
        partial: bool = True,
) -> EventResponseSchema:
    stmt = (
        select(EventModel)
        .options(joinedload(EventModel.tags))
        .where(EventModel.id == event_id)
    )
    result = await session.execute(stmt)
    event = result.scalars().first()

    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")

    update_data = event_update_schema.model_dump(exclude_unset=partial)

    for key, value in update_data.items():
        if key == "tags" and isinstance(value, list):
            related_tags = await session.execute(
                select(TagModel).where(TagModel.id.in_(value))
            )
            setattr(event, key, related_tags.scalars().all())
        elif isinstance(value, datetime):
            setattr(event, key, make_naive(value))
        else:
            setattr(event, key, value)

    await session.commit()
    await session.refresh(event)

    return EventResponseSchema(
        id=event.id,
        title=event.title,
        description=event.description,
        start_data=event.start_data,
        end_data=event.end_data,
        location=event.location,
        is_active=event.is_active,
        number_of_tickets=event.number_of_tickets,
        organizer_name=event.organizer_name,
        organizer_email=event.organizer_email,
        tags=[tag.name for tag in event.tags]
    )


async def delete_event_crud(
        event_id: UUID,
        session: AsyncSession,
):
    stmt = (
        select(EventModel)
        .options(joinedload(EventModel.tags))
        .where(EventModel.id == event_id)
    )
    result = await session.execute(stmt)
    event = result.scalars().first()

    if not event:
        return f"Event with id {event_id} not found"

    await session.delete(event)
    await session.commit()
    return f"Event {event_id} deleted"