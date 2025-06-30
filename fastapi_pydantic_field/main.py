from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class BookSchema(BaseModel):
    title: str = Field(..., description="タイトルの指定：必須", examples=["速習FastAPI"])
    category: str = Field(..., description="カテゴリの指定：必須", examples=["technical"])
    publish_year: Optional[int] = Field(default=None, description="出版年の指定：任意", examples=[2023])
    price: float = Field(..., gt=0, le=5000, description="価格の指定:0 < 価格 <= 5000", examples=[2500])

@app.post("/books/", response_model=BookSchema)
async def create_book(book: BookSchema):
    return book