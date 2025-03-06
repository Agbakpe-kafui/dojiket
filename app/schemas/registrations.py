from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from decimal import Decimal
from typing import List

class EventFormFieldBase(BaseModel):
    field_name: str
    field_label: str
    field_type: str
    is_required: bool = False
    validation_rules: dict | None
    field_options: dict | None
    display_order: int

class EventFormFieldCreate(EventFormFieldBase):
    pass

class EventFormField(EventFormFieldBase):
    id: UUID
    event_id: UUID

    class Config:
        orm_mode = True

class EventFormResponseBase(BaseModel):
    response_value: str

class EventFormResponseCreate(EventFormResponseBase):
    form_field_id: UUID

class EventFormResponse(EventFormResponseBase):
    id: UUID
    registration_id: UUID
    form_field_id: UUID
    created_at: datetime

    class Config:
        orm_mode = True

class RegistrationBase(BaseModel):
    status: str
    amount_paid: Decimal

class RegistrationCreate(RegistrationBase):
    event_id: UUID

class Registration(RegistrationBase):
    id: UUID
    event_id: UUID
    user_id: UUID
    registration_date: datetime
    created_at: datetime
    updated_at: datetime
    form_responses: List[EventFormResponse] = []

    class Config:
        orm_mode = True 