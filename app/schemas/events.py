from pydantic import BaseModel
from datetime import datetime
from uuid import UUID
from decimal import Decimal

class EventBase(BaseModel):
    title: str
    description: str
    event_date: datetime
    capacity: int
    price: Decimal
    is_active: bool = True

class EventCreate(EventBase):
    venue_id: UUID | None = None

class Event(EventBase):
    id: UUID
    creator_id: UUID
    venue_id: UUID | None
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 