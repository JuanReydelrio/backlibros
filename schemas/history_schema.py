from pydantic import BaseModel
from datetime import datetime

class HistoryCreate(BaseModel):
    book_id: str


class HistoryResponse(BaseModel):
    id: int
    book_id: str
    visited_at: datetime

    class Config:
        from_attributes = True
        