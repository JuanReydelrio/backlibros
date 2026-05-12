from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db

from schemas.book_schema import BookCreate, BookUpdate, BookResponse
from crud.crud_books import get_books, get_book, create_book, update_book, delete_book
from security import get_current_user

router = APIRouter(prefix="/books", tags=["Books"])

# 🔹 LISTAR
@router.get("/", response_model=list[BookResponse])
def list_books(db: Session = Depends(get_db)):
    return get_books(db)

# 🔹 OBTENER UNO
@router.get("/{book_id}", response_model=BookResponse)
def get_one(book_id: str, db: Session = Depends(get_db)):
    book = get_book(db, book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return book

# 🔹 CREAR
@router.post("/", response_model=BookResponse)
def create(data: BookCreate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    book = create_book(db, data)
    if not book:
        raise HTTPException(status_code=400, detail="Categoría inválida")
    return book

# 🔹 ACTUALIZAR
@router.put("/{book_id}", response_model=BookResponse)
def update(book_id: str, data: BookUpdate, db: Session = Depends(get_db), user=Depends(get_current_user)):
    book = update_book(db, book_id, data)
    if not book:
        raise HTTPException(status_code=400, detail="Libro o categoría inválida")
    return book

# 🔹 ELIMINAR
@router.delete("/{book_id}")
def delete(book_id: str, db: Session = Depends(get_db), user=Depends(get_current_user)):
    ok = delete_book(db, book_id)
    if not ok:
        raise HTTPException(status_code=404, detail="Libro no encontrado")
    return {"message": "Libro eliminado"}