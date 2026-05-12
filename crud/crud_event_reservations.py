from sqlalchemy.orm import Session
from models.event_reservation_model import EventReservation
from models.event_model import Event


# 🔍 Obtener una reserva específica
def get_reservation(db: Session, user_id: str, event_id: str):
    return (
        db.query(EventReservation)
        .filter(
            EventReservation.user_id == user_id,
            EventReservation.event_id == event_id
        )
        .first()
    )


# 🔢 Contar reservas de un evento
def count_event_reservations(db: Session, event_id: str):
    return (
        db.query(EventReservation)
        .filter(EventReservation.event_id == event_id)
        .count()
    )


# 🎟 Crear reserva
def reserve_event(db: Session, user_id: str, event_id: str):

    event = db.query(Event).filter(Event.id == event_id).first()
    if not event:
        return None, "Evento no encontrado"

    # evitar duplicado
    existing = get_reservation(db, user_id, event_id)
    if existing:
        return None, "Ya tienes una reserva en este evento"

    # validar capacidad
    total = count_event_reservations(db, event_id)
    if total >= event.capacity:
        return None, "Evento lleno"

    reservation = EventReservation(
        user_id=user_id,
        event_id=event_id
    )

    db.add(reservation)
    db.commit()
    db.refresh(reservation)

    return reservation, None


# ❌ Cancelar reserva
def cancel_reservation(db: Session, user_id: str, event_id: str):
    reservation = get_reservation(db, user_id, event_id)

    if not reservation:
        return None

    db.delete(reservation)
    db.commit()
    return reservation


# 📋 Mis reservas (DETALLADO 🔥)
def get_my_reservations(db: Session, user_id: str):

    results = (
        db.query(EventReservation, Event)
        .join(Event, Event.id == EventReservation.event_id)
        .filter(EventReservation.user_id == user_id)
        .all()
    )

    return [
        {
            "event_id": e.id,
            "event_name": e.name,
            "event_date": e.event_date,
            "event_time": e.event_time,
            "place": e.place,
            "registered_at": r.registered_at
        }
        for r, e in results
    ]