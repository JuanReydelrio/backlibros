from sqlalchemy.orm import Session
from sqlalchemy import text
from models.history_model import History


def add_or_update_history(db: Session, user_id: str, book_id: str):
    # 🔥 UPSERT (clave del parcial)
    query = text("""
        INSERT INTO history (user_id, book_id)
        VALUES (:user_id, :book_id)
        ON DUPLICATE KEY UPDATE visited_at = CURRENT_TIMESTAMP
    """)

    db.execute(query, {"user_id": user_id, "book_id": book_id})
    db.commit()


def get_user_history(db: Session, user_id: str):
    return (
        db.query(History)
        .filter(History.user_id == user_id)
        .order_by(History.visited_at.desc())
        .all()
    )


def delete_from_history(db: Session, user_id: str, book_id: str):
    history = (
        db.query(History)
        .filter(History.user_id == user_id, History.book_id == book_id)
        .first()
    )

    if history:
        db.delete(history)
        db.commit()

    return history