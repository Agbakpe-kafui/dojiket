from pydantic import BaseModel
from datetime import datetime
from uuid import UUID

class VenueBase(BaseModel):
    name: str
    address: str
    capacity: int
    amenities: str | None
    is_active: bool = True

class VenueCreate(VenueBase):
    pass

class Venue(VenueBase):
    id: UUID
    owner_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True 