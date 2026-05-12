from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, text, UniqueConstraint
from database import Base


class History(Base):
    __tablename__ = "history"
    __table_args__ = (
        UniqueConstraint("user_id", "book_id", name="unique_user_book"),
    )

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    book_id = Column(String(36), ForeignKey("books.id", ondelete="CASCADE"), nullable=False)
    visited_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))