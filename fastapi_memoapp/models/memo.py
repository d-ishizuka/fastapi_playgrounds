from sqlalchemy import Column, Integer, String, DateTime
from db import Base
from datetime import datetime

class Memo(Base):
    __tablename__ = "memos"
    memo_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    description = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime)