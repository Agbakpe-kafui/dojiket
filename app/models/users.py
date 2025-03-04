from sqlalchemy import Boolean, Column, Integer, String, Enum
from database import Base
import enum
from sqlalchemy.orm import relationship

class UserType(str, enum.Enum):
    REGULAR = "regular"
    VENUE_OWNER = "venue_owner"

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    full_name = Column(String)
    user_type = Column(Enum(UserType))
    is_active = Column(Boolean, default=True)
    events = relationship("Event", back_populates="creator")
    venues = relationship("Venue", back_populates="owner")
    registrations = relationship("EventRegistration", back_populates="user")
