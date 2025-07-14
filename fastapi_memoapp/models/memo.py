from typing import Optional
from pickle import TRUE
from sqlalchemy import Column, Integer, String, DateTime, func, Boolean
from db import Base
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column

class Memo(Base):
    __tablename__ = "memos"
    memo_id:Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    description: Mapped[str] = mapped_column(String(255), nullable=True)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    priority: Mapped[str] = mapped_column(String(10), nullable=False)
    due_date: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)