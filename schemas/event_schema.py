from pydantic import BaseModel
from datetime import date, time

class EventCreate(BaseModel):
    name: str
    description: str | None = None
    event_date: date
    event_time: time
    place: str
    moderator: str
    capacity: int = 30


class EventResponse(BaseModel):
    id: str
    name: str
    description: str | None
    event_date: date
    event_time: time
    place: str
    moderator: str
    capacity: int

    class Config:
        from_attributes = True