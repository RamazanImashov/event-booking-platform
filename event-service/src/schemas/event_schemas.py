from typing import List, Optional
from uuid import UUID
from pydantic import BaseModel, Field, ConfigDict, root_validator
from datetime import datetime


class EventBaseSchema(BaseModel):
    title: Optional[str] = Field(..., max_length=255, description="Название события")
    description: Optional[str] = Field(None, description="Описание события")
    start_data: Optional[datetime] = Field(..., description="Дата и время начала события")
    end_data: Optional[datetime] = Field(..., description="Дата и время окончания события")
    location: Optional[str] = Field(..., max_length=255, description="Местоположение события")
    number_of_tickets: Optional[int] = Field(..., description="Количество билетов")
    is_active: Optional[bool] = Field(default=True, description="Активно ли событие")
    organizer_name: Optional[str] = Field(..., description="Наименование Организации")
    organizer_email: Optional[str] = Field(..., description="Email почта организации")

    model_config = ConfigDict(from_attributes=True)


class EventCreateSchema(EventBaseSchema):
    tags: list[UUID] = Field(default=[], description="Список идентификаторов тегов")
    organizer_id: Optional[str] = Field(..., description="Идентификатор организации")

    class Config:
        orm_mode = True


class EventUpdateSchema(BaseModel):
    title: Optional[str] = Field(None, max_length=255, description="Название события")
    description: Optional[str] = Field(None, description="Описание события")
    start_date: Optional[datetime] = Field(None, description="Дата и время начала события")
    end_date: Optional[datetime] = Field(None, description="Дата и время окончания события")
    location: Optional[str] = Field(None, max_length=255, description="Местоположение события")
    is_active: Optional[bool] = Field(None, description="Активно ли событие")
    number_of_tickets: Optional[int] = Field(..., description="Количество билетов")
    tags: Optional[List[UUID]] = Field(None, description="Список идентификаторов тегов")

    model_config = ConfigDict(from_attributes=True)

    @root_validator(pre=True)
    def validate_dates(cls, values):
        if 'start_data' in values and values['start_data'].tzinfo is not None:
            values['start_data'] = values['start_data'].astimezone(None).replace(tzinfo=None)
        if 'end_data' in values and values['end_data'].tzinfo is not None:
            values['end_data'] = values['end_data'].astimezone(None).replace(tzinfo=None)
        return values


class EventUpdateSchemaP(BaseModel):
    title: Optional[str] = Field(None, max_length=255, description="Название события")
    description: Optional[str] = Field(None, description="Описание события")
    start_date: Optional[datetime] = Field(None, description="Дата и время начала события")
    end_date: Optional[datetime] = Field(None, description="Дата и время окончания события")
    location: Optional[str] = Field(None, max_length=255, description="Местоположение события")
    is_active: Optional[bool] = Field(None, description="Активно ли событие")
    number_of_tickets: Optional[int] = Field(..., description="Количество билетов")
    tags: Optional[List[UUID]] = Field(None, description="Список идентификаторов тегов")

    class Config:
        orm_mode = True

    @root_validator(pre=True)
    def validate_dates(cls, values):
        if 'start_date' in values and values['start_date'] and values['start_date'].tzinfo is not None:
            values['start_date'] = values['start_date'].astimezone(None).replace(tzinfo=None)
        if 'end_date' in values and values['end_date'] and values['end_date'].tzinfo is not None:
            values['end_date'] = values['end_date'].astimezone(None).replace(tzinfo=None)
        return values


class EventResponseSchema(EventBaseSchema):
    id: UUID = Field(..., description="Идентификатор события")
    created_at: Optional[datetime] = Field(..., description="Дата и время создания события")
    tags: List[str] = Field(default=[], description="Список имен тегов")

    model_config = ConfigDict(from_attributes=True)

