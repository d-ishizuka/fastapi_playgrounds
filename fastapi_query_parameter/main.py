from socket import gaierror
from token import OP
from fastapi import FastAPI
from typing import Optional
from data import get_books_by_category

app = FastAPI()

@app.get("/books/")
async def read_books(
    category: Optional[str] = None
    ) -> list[dict[str, str]]:
    result = get_books_by_category(category)
    
    return [{
        "id": book.id,
        "title": book.title,
        "category": book.category
        } for book in result]