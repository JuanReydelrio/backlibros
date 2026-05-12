from sqlalchemy.orm import Session
from models.book_model import Book
from models.category_model import Category
import uuid


def get_books(db: Session):
    return db.query(Book).all()


def get_book(db: Session, book_id: str):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, data):
    # Validar categoría
    category = db.query(Category).filter(Category.id == data.category_id).first()
    if not category:
        return None

    book = Book(
        id=str(uuid.uuid4()),
        title=data.title,
        author=data.author,
        pages=data.pages,
        category_id=data.category_id
    )

    db.add(book)
    db.commit()
    db.refresh(book)
    return book


def update_book(db: Session, book_id: str, data):
    book = get_book(db, book_id)
    if not book:
        return None

    category = db.query(Category).filter(Category.id == data.category_id).first()
    if not category:
        return None

    book.title = data.title
    book.author = data.author
    book.pages = data.pages
    book.category_id = data.category_id

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: str):
    book = get_book(db, book_id)
    if not book:
        return None

    db.delete(book)
    db.commit()
    return True