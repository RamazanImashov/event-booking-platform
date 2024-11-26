from uuid import UUID
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime


class TagBaseSchema(BaseModel):
    name: str = Field(..., max_length=50, description="Название тега")

    model_config = ConfigDict(from_attributes=True)


class TagCreateSchema(TagBaseSchema):
    class Config:
        orm_mode = True


class TagUpdateSchema(BaseModel):
    name: Optional[str] = Field(None, max_length=50, description="Новое название тега")

    class Config:
        orm_mode = True


class TagResponseSchema(TagBaseSchema):
    id: UUID = Field(..., description="Идентификатор тега")
    created_at: datetime = Field(..., description="Дата создания тега")

    model_config = ConfigDict(from_attributes=True)
