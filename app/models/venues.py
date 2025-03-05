from sqlalchemy import Boolean, Column, Integer, String, DateTime, ForeignKey, Text, UUID
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base
import uuid

class Venue(Base):
    __tablename__ = "venues"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    owner_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    capacity = Column(Integer)
    amenities = Column(Text)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    owner = relationship("User", back_populates="venues")
    events = relationship("Event", back_populates="venue") 