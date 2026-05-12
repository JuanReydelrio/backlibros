from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from crud import crud_history
from schemas.history_schema import HistoryCreate, HistoryResponse
from security import get_current_user
from models.user_model import User

router = APIRouter(prefix="/history", tags=["History"])


# ✅ AGREGAR O ACTUALIZAR
@router.post("/{book_id}", status_code=200)
def add_or_update_history(
    book_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    crud_history.add_or_update_history(db, current_user.id, book_id)

    return {"message": "Historial actualizado"}


# ✅ LISTAR HISTORIAL
@router.get("/", response_model=list[HistoryResponse])
def get_history(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return crud_history.get_user_history(db, current_user.id)


# ✅ ELIMINAR DEL HISTORIAL
@router.delete("/{book_id}")
def delete_history(
    book_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    history = crud_history.delete_from_history(db, current_user.id, book_id)

    if not history:
        raise HTTPException(status_code=404, detail="No existe en historial")

    return {"message": "Eliminado del historial"}