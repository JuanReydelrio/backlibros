from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from crud.crud_favorites import add_favorite, remove_favorite, get_favorites
from schemas.favorite_schema import FavoriteResponse
from security import get_current_user

router = APIRouter(prefix="/favorites", tags=["Favorites"])


# ⭐ AGREGAR FAVORITO
@router.post("/{book_id}", response_model=FavoriteResponse)
def add(book_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    fav = add_favorite(db, user.id, book_id)
    if not fav:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return fav


# ❌ ELIMINAR FAVORITO
@router.delete("/{book_id}")
def remove(book_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = remove_favorite(db, user.id, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Favorito no encontrado")
    return {"message": "Eliminado de favoritos"}


# 📚 LISTAR FAVORITOS
@router.get("/", response_model=list[FavoriteResponse])
def list_favorites(db: Session = Depends(get_db), user=Depends(get_current_user)):
    return get_favorites(db, user.id)