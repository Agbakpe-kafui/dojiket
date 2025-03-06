from sqlalchemy import Boolean, Column, String, Enum, UUID, DateTime
from ..database import Base
import enum
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

class UserType(str, enum.Enum):
    REGULAR = "regular"
    VENUE_OWNER = "venue_owner"

class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    phone = Column(String, nullable=True)
    user_type = Column(Enum(UserType))
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    events = relationship("Event", back_populates="creator")
    venues = relationship("Venue", back_populates="owner")
    registrations = relationship("EventRegistration", back_populates="user")
