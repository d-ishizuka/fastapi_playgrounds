from pydantic import BaseModel

class BookSchema(BaseModel):
    title: str
    category: str

class BookResponseShema(BookSchema):
    id: int