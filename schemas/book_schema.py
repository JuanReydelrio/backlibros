from pydantic import BaseModel
from datetime import datetime

class BookCreate(BaseModel):
    title: str
    author: str
    pages: int
    category_id: int

class BookUpdate(BaseModel):
    title: str
    author: str
    pages: int
    category_id: int

class CategoryOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    pages: int
    category: CategoryOut
    created_at: datetime

    class Config:
        from_attributes = True