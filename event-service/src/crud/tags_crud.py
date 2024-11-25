
from typing import Sequence

from uuid import UUID

from fastapi import HTTPException, Request

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..models.tag_models import TagModel

from src.schemas.tags_schemas import TagCreateSchema, TagResponseSchema


async def get_all_tags_crud(
        session: AsyncSession
) -> Sequence[TagModel]:
    stmt = select(TagModel).order_by(TagModel.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_id_tag_crud(
        tags_id: UUID,
        session: AsyncSession
) -> Sequence[TagModel]:
    stmt = select(TagModel).where(TagModel.id == tags_id)
    result = await session.scalars(stmt)
    tag = result.first()
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tag


async def create_tag_crud(
        session: AsyncSession,
        tag_create_schema: TagCreateSchema
) -> TagModel:
    tag = TagModel(**tag_create_schema.model_dump())
    session.add(tag)
    await session.commit()
    await session.refresh(tag)
    return tag
