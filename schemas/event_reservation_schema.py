from pydantic import BaseModel
from datetime import datetime, date, time


# Crear (aunque no se usa mucho porque el user sale del token)
class EventReservationCreate(BaseModel):
    event_id: str


# Respuesta básica
class EventReservationResponse(BaseModel):
    user_id: str
    event_id: str
    registered_at: datetime

    class Config:
        from_attributes = True


# Respuesta enriquecida (recomendada 🔥)
class EventReservationDetail(BaseModel):
    event_id: str
    event_name: str
    event_date: date
    event_time: time
    place: str
    registered_at: datetime

    class Config:
        from_attributes = True