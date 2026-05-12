from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from security import get_current_user
from models.user_model import User

from crud.crud_event_reservations import (
    reserve_event,
    cancel_reservation,
    get_my_reservations
)

from schemas.event_reservation_schema import (
    EventReservationResponse,
    EventReservationDetail
)

router = APIRouter(prefix="/event-reservations", tags=["Event Reservations"])


# 🎟 Reservar evento (usa token)
@router.post("/{event_id}", response_model=EventReservationResponse)
def reserve(
    event_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    reservation, error = reserve_event(db, current_user.id, event_id)

    if not reservation:
        raise HTTPException(status_code=400, detail=error)

    return reservation


# ❌ Cancelar reserva
@router.delete("/{event_id}")
def cancel(
    event_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    reservation = cancel_reservation(db, current_user.id, event_id)

    if not reservation:
        raise HTTPException(status_code=404, detail="Reserva no encontrada")

    return {"message": "Reserva cancelada"}


# 📋 Mis reservas (DETALLE)
@router.get("/me", response_model=list[EventReservationDetail])
def my_reservations(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return get_my_reservations(db, current_user.id)
