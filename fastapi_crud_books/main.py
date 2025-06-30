from fastapi import FastAPI, HTTPException
from book_schemas import BookSchema, BookResponseShema

app = FastAPI()

books: list[BookResponseShema] = [
    BookResponseShema(id=1, title="Python入門", category="technical"),
    BookResponseShema(id=2, title="はじめてのプログラミング", category="technical"),
    BookResponseShema(id=3, title="すすむ巨人", category="comics"),
    BookResponseShema(id=4, title="DBおやじ", category="comics"),
    BookResponseShema(id=5, title="週刊ダイヤモンド", category="magazine"),
    BookResponseShema(id=6, title="ザ・社長", category="magazine"), 
]

@app.post("/books/", response_model=BookResponseShema)
def create_book(book: BookSchema):
    new_book_id = max([book.id for book in books], default=0) + 1
    new_book = BookResponseShema(id=new_book_id, **book.model_dump())
    books.append(new_book)
    return new_book

@app.get("/books/", response_model=list[BookResponseShema])
def read_books():
    return books

@app.get("/books/{book_id}", response_model=BookResponseShema)
def read_book(book_id: int):
    for book in books:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail="Book not found")

@app.put("/books/{book_id}", response_model=BookResponseShema)
def update_book(book_id: int, book: BookSchema):
    for index, existing_book in enumerate(books):
        if existing_book.id == book_id:
            updated_book = BookResponseShema(id=book_id, **book.model_dump())
            books[index] = updated_book
            return updated_book
    raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{book_id}", response_model=BookResponseShema)
def delete_book(book_id: int):
    for index, book in enumerate(books):
        if book.id == book_id:
            books.pop(index)
            return book
    raise HTTPException(status_code=404, detail="Book not found")