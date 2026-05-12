from sqlalchemy import Column, String, ForeignKey, TIMESTAMP, text
from database import Base


class EventReservation(Base):
    __tablename__ = "event_reservations"

    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    event_id = Column(String(36), ForeignKey("events.id", ondelete="CASCADE"), primary_key=True)
    registered_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))