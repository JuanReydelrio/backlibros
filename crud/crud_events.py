import uuid
from sqlalchemy.orm import Session
from models.event_model import Event


def create_event(db: Session, data):
    new_event = Event(
        id=str(uuid.uuid4()),
        name=data.name,
        description=data.description,
        event_date=data.event_date,
        event_time=data.event_time,
        place=data.place,
        moderator=data.moderator,
        capacity=data.capacity
    )

    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event

def update_event(db: Session, event_id: str, data):
    event = get_event(db, event_id)
    if not event:
        return None

    event.name = data.name
    event.description = data.description
    event.event_date = data.event_date
    event.event_time = data.event_time
    event.place = data.place
    event.moderator = data.moderator
    event.capacity = data.capacity

    db.commit()
    db.refresh(event)
    return event

def get_events(db: Session):
    return db.query(Event).order_by(Event.event_date, Event.event_time).all()


def get_event(db: Session, event_id: str):
    return db.query(Event).filter(Event.id == event_id).first()


def delete_event(db: Session, event_id: str):
    event = get_event(db, event_id)
    if event:
        db.delete(event)
        db.commit()
    return event