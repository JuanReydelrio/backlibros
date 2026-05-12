from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.category_schema import CategoryCreate, CategoryUpdate, CategoryResponse
from crud.crud_categories import (
    get_categories,
    get_category,
    get_category_by_name,
    create_category,
    update_category,
    delete_category
)

from security import get_current_user

router = APIRouter(prefix="/categories", tags=["Categories"])

# 🔹 LISTAR
@router.get("/", response_model=list[CategoryResponse])
def list_categories(db: Session = Depends(get_db)):
    return get_categories(db)

# 🔹 OBTENER UNA
@router.get("/{category_id}", response_model=CategoryResponse)
def get_one(category_id: int, db: Session = Depends(get_db)):
    category = get_category(db, category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")
    return category

# 🔹 CREAR (PROTEGIDO)
@router.post("/", response_model=CategoryResponse)
def create(data: CategoryCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):

    existing = get_category_by_name(db, data.name)
    if existing:
        raise HTTPException(status_code=400, detail="Categoría ya existe")

    return create_category(db, data.name)

# 🔹 ACTUALIZAR
@router.put("/{category_id}", response_model=CategoryResponse)
def update(category_id: int, data: CategoryUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):

    category = update_category(db, category_id, data.name)
    if not category:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    return category

# 🔹 ELIMINAR
@router.delete("/{category_id}")
def delete(category_id: int, db: Session = Depends(get_db), user=Depends(get_current_user)):

    ok = delete_category(db, category_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Categoría no encontrada")

    return {"message": "Categoría eliminada"}