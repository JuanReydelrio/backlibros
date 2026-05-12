from sqlalchemy.orm import Session
from models.category_model import Category

def get_categories(db: Session):
    return db.query(Category).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def get_category_by_name(db: Session, name: str):
    return db.query(Category).filter(Category.name == name).first()

def create_category(db: Session, name: str):
    category = Category(name=name)
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(db: Session, category_id: int, name: str):
    category = get_category(db, category_id)
    if not category:
        return None

    category.name = name
    db.commit()
    db.refresh(category)
    return category

def delete_category(db: Session, category_id: int):
    category = get_category(db, category_id)
    if not category:
        return None

    db.delete(category)
    db.commit()
    return True
    