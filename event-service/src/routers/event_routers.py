from fastapi import APIRouter, Depends, Request, status
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Annotated
from src.schemas.event_schemas import (
    EventCreateSchema,
    EventResponseSchema,
    EventUpdateSchema,
    EventUpdateSchemaP
)
from src.crud.event_crud import (
    get_all_events_crud, create_event_crud,
    get_id_event_crud, update_event_crud,
    partial_update_event_crud, delete_event_crud
)

from src.helper.database import db_helper

router = APIRouter(
    prefix="/events",
    tags=["Events"]
)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_event(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        event_create: EventCreateSchema
):
    event = await create_event_crud(
        session=session,
        event_create_schema=event_create
    )
    return {
        "status code": status.HTTP_201_CREATED,
        "message": "Event created successfully",
        "event": event
    }


@router.get("/", response_model=List[EventResponseSchema], status_code=status.HTTP_200_OK)
async def get_all_events(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],):
    events = await get_all_events_crud(session)
    return events


@router.get("/{event_id}/", response_model=EventResponseSchema, status_code=status.HTTP_200_OK)
async def get_event_id(
        event_id: UUID,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ]
) -> EventResponseSchema:
    event = await get_id_event_crud(event_id=event_id, session=session)
    return event


@router.put("/{event_id}/", response_model=EventResponseSchema, status_code=status.HTTP_206_PARTIAL_CONTENT)
async def put_update_event(
    event_id: UUID,
    event_update: EventUpdateSchema,
    session: Annotated[AsyncSession, Depends(db_helper.session_getter)],
):
    return await update_event_crud(
        event_id=event_id,
        session=session,
        event_update_schema=event_update,
    )


@router.patch("/{event_id}/", response_model=EventResponseSchema, status_code=status.HTTP_206_PARTIAL_CONTENT)
async def patch_update_event(
    event_id: UUID,
    event_update: EventUpdateSchemaP,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await partial_update_event_crud(
        event_id=event_id,
        session=session,
        event_update_schema=event_update,
        partial=True,
    )


@router.delete("/{event_id}/", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    event_id: UUID,
    session: Annotated[
        AsyncSession,
        Depends(db_helper.session_getter),
    ],
):
    return await delete_event_crud(
        event_id=event_id,
        session=session,
    )
