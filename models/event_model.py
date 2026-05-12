from sqlalchemy import Column, String, Integer, Text, Date, Time, TIMESTAMP, text
from database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(String(36), primary_key=True, index=True)
    name = Column(String(150), nullable=False)
    description = Column(Text, nullable=True)
    event_date = Column(Date, nullable=False)
    event_time = Column(Time, nullable=False)
    place = Column(String(100), nullable=False)
    moderator = Column(String(100), nullable=False)
    capacity = Column(Integer, default=30)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))