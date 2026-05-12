from sqlalchemy.orm import Session
from models.favorite_model import Favorite
from models.book_model import Book

# 🔹 AGREGAR FAVORITO
def add_favorite(db: Session, user_id: str, book_id: str):
    # validar libro
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None

    # evitar duplicados
    existing = db.query(Favorite).filter(
        Favorite.user_id == user_id,
        Favorite.book_id == book_id
    ).first()

    if existing:
        return existing

    favorite = Favorite(user_id=user_id, book_id=book_id)
    db.add(favorite)
    db.commit()
    db.refresh(favorite)
    return favorite


# 🔹 ELIMINAR FAVORITO
def remove_favorite(db: Session, user_id: str, book_id: str):
    fav = db.query(Favorite).filter(
        Favorite.user_id == user_id,
        Favorite.book_id == book_id
    ).first()

    if not fav:
        return None

    db.delete(fav)
    db.commit()
    return True


# 🔹 LISTAR FAVORITOS
def get_favorites(db: Session, user_id: str):
    return db.query(Favorite).filter(Favorite.user_id == user_id).all()