from pydantic import BaseModel
from datetime import datetime

class FavoriteResponse(BaseModel):
    book_id: str
    created_at: datetime

    class Config:
        from_attributes = True