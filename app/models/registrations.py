from sqlalchemy import Column, Integer, String, Numeric, DateTime, ForeignKey, Text, UUID, Enum, Boolean, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base
import uuid
import enum

class RegistrationStatus(str, enum.Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class FieldType(str, enum.Enum):
    TEXT = "text"
    NUMBER = "number"
    SELECT = "select"
    DATE = "date"
    EMAIL = "email"

class EventRegistration(Base):
    __tablename__ = "event_registrations"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID, ForeignKey("events.id"), nullable=False)
    user_id = Column(UUID, ForeignKey("users.id"), nullable=False)
    registration_date = Column(DateTime, default=datetime.utcnow)
    status = Column(String)  # According to ER diagram
    amount_paid = Column(Numeric(10, 2), default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    event = relationship("Event", back_populates="registrations")
    user = relationship("User", back_populates="registrations")
    form_responses = relationship("EventFormResponse", back_populates="registration")

class EventFormField(Base):
    __tablename__ = "event_form_fields"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    event_id = Column(UUID, ForeignKey("events.id"), nullable=False)
    field_name = Column(String, nullable=False)
    field_label = Column(String, nullable=False)
    field_type = Column(String, nullable=False)
    is_required = Column(Boolean, default=False)
    validation_rules = Column(JSON, nullable=True)
    field_options = Column(JSON, nullable=True)
    display_order = Column(Integer)

    # Relationships
    event = relationship("Event", back_populates="form_fields")
    responses = relationship("EventFormResponse", back_populates="form_field")

class EventFormResponse(Base):
    __tablename__ = "event_form_responses"

    id = Column(UUID, primary_key=True, default=uuid.uuid4)
    registration_id = Column(UUID, ForeignKey("event_registrations.id"), nullable=False)
    form_field_id = Column(UUID, ForeignKey("event_form_fields.id"), nullable=False)
    response_value = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    registration = relationship("EventRegistration", back_populates="form_responses")
    form_field = relationship("EventFormField", back_populates="responses") 