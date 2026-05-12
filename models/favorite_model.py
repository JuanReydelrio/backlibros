from sqlalchemy import Column, String, ForeignKey, TIMESTAMP
from sqlalchemy.sql import func
from database import Base

class Favorite(Base):
    __tablename__ = "favorites"

    user_id = Column(String(36), ForeignKey("users.id"), primary_key=True)
    book_id = Column(String(36), ForeignKey("books.id"), primary_key=True)
    created_at = Column(TIMESTAMP, server_default=func.now())