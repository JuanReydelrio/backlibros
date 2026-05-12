from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.event_schema import EventCreate, EventResponse
from crud.crud_events import create_event, get_events, get_event, delete_event, update_event
from security import get_current_user   

router = APIRouter(prefix="/events", tags=["Events"])


# Listar eventos
@router.get("/", response_model=list[EventResponse])
def list_events(db: Session = Depends(get_db)):
    return get_events(db)


# Obtener un evento
@router.get("/{event_id}", response_model=EventResponse)
def get_one(event_id: str, db: Session = Depends(get_db)):
    event = get_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return event

# editar evento (protegido)
@router.put("/{event_id}", response_model=EventResponse)
def update(event_id: str, data: EventCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    event = update_event(db, event_id, data)
    if not event:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return event


# Crear evento (protegido)
@router.post("/", response_model=EventResponse)
def create(data: EventCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    return create_event(db, data)


# Eliminar evento (protegido)
@router.delete("/{event_id}")
def delete(event_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    event = delete_event(db, event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return {"message": "Evento eliminado"}