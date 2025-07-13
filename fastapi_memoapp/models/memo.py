from sqlalchemy import Column, Integer, String, DateTime, func
from db import Base
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

class Memo(Base):
    __tablename__ = "memos"
    memo_id = Column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    created_at = Column(DateTime, default=datetime.now())