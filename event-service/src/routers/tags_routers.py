from fastapi import APIRouter, Depends, Request, status
from uuid import UUID
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Annotated
from src.schemas.tags_schemas import TagCreateSchema, TagResponseSchema
from src.crud.tags_crud import get_all_tags_crud, create_tag_crud, get_id_tag_crud
from src.models.tag_models import TagModel
from src.helper.database import db_helper
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ValidationException
from fastapi.responses import JSONResponse, FileResponse

router = APIRouter(
    prefix="/tags",
    tags=["Tags"]
)


@router.post("/")
async def create_tag(
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ],
        tag_create: TagCreateSchema
):
    tag = await create_tag_crud(
        session=session,
        tag_create_schema=tag_create
    )
    return {
        "status code": status.HTTP_201_CREATED,
        "message": "Tag created successfully",
        "tag": tag
    }


@router.get("/", response_model=List[TagResponseSchema])
async def get_all_tags(session: Annotated[AsyncSession, Depends(db_helper.session_getter)],):
    tags = await get_all_tags_crud(session)
    return tags


@router.get("/{tags_id}/", response_model=TagResponseSchema)
async def get_tag_id(
        tags_id: UUID,
        session: Annotated[
            AsyncSession,
            Depends(db_helper.session_getter),
        ]
) -> TagResponseSchema:
    tag = await get_id_tag_crud(tags_id=tags_id, session=session)
    return tag