from pydantic import BaseModel, EmailStr
from datetime import datetime

# 🔹 CREAR USUARIO
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

# 🔹 LOGIN
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# 🔹 ACTUALIZAR PERFIL
class UserUpdate(BaseModel):
    name: str
    email: EmailStr

# 🔹 RESPUESTA
class UserResponse(BaseModel):
    id: str
    name: str
    email: EmailStr
    created_at: datetime

    class Config:
        from_attributes = True