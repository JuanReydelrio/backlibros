from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.user_schema import UserUpdate, UserResponse
from crud.crud_users import get_user_by_id, get_user_by_email, update_user
from security import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])

# 🔹 VER PERFIL
@router.get("/me", response_model=UserResponse)
def get_me(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    user = get_user_by_id(db, current_user.id)
    return user

# 🔹 ACTUALIZAR PERFIL
@router.put("/me", response_model=UserResponse)
def update_me(data: UserUpdate, db: Session = Depends(get_db), current_user=Depends(get_current_user)):

    # 🔥 validar email único
    existing = get_user_by_email(db, data.email)
    if existing and existing.id != current_user.id:
        raise HTTPException(status_code=400, detail="Email ya en uso")

    user = update_user(db, current_user.id, data.name, data.email)

    if not user:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    return user
