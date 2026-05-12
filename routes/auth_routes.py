from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.user_schema import UserCreate, UserLogin, UserResponse
from crud.crud_users import create_user, authenticate_user, get_user_by_email
from security import create_access_token, get_current_user

router = APIRouter(prefix="/auth", tags=["Auth"])

# 🔹 REGISTRO
@router.post("/register", response_model=UserResponse)
def register(user: UserCreate, db: Session = Depends(get_db)):
    
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    new_user = create_user(db, user.name, user.email, user.password)
    return new_user

# 🔹 LOGIN
@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    
    db_user = authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    token = create_access_token({"sub": db_user.id})
    
    return {
        "access_token": token,
        "token_type": "bearer"
    }

# 🔹 USUARIO ACTUAL
@router.get("/me", response_model=UserResponse)
def get_me(current_user = Depends(get_current_user)):
    return current_user