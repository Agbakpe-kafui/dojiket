from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey, Text, UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base
import uuid

class Event(Base):
    __tablename__ = "events"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    creator_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    venue_id = Column(UUID, ForeignKey("venues.id"), nullable=True)
    title = Column(String, nullable=False)
    description = Column(Text)
    event_date = Column(DateTime, nullable=False)
    capacity = Column(Integer)
    price = Column(Float, default=0.0)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    creator = relationship("User", back_populates="events")
    venue = relationship("Venue", back_populates="events")
    registrations = relationship("EventRegistration", back_populates="event")
    form_fields = relationship("EventFormField", back_populates="event") 