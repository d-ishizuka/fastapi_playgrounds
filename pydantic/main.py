from datetime import datetime
from pydantic import BaseModel, ValidationError

class Event(BaseModel):
    name: str = "未定"
    start_datetime: datetime
    participants: list[str] = []

external_data = {
    "name": "FastAPI勉強会",
    "start_datetime": "2023-07-07 07:00",
    "participants": ["山田", "鈴木", "田中"]
}

try:
    event = Event(**external_data)
    print("イベント名:", event.name, type(event.name))
    print("開催日時", event.start_datetime, type(event.start_datetime))
    print("参加者:", event.participants, type(event.participants))
except ValidationError as e:
    print("データのバリデーションエラーが発生しました:", e.errors())