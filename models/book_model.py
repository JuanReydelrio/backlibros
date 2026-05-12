from sqlalchemy import Column, String, Integer, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class Book(Base):
    __tablename__ = "books"

    id = Column(String(36), primary_key=True)
    title = Column(String(150), nullable=False)
    author = Column(String(100), nullable=False)
    pages = Column(Integer, nullable=False, default=0)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    category = relationship("Category")