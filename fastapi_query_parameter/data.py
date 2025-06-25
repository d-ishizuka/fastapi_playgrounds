from typing import Optional

class Book:
    def __init__(self, id: str, title: str, category: str):
        self.id = id
        self.title = title
        self.category = category

books = [
    Book(id="1", title="Python入門", category="technical"),
    Book(id="2", title="はじめてのプログラミング", category="technical"),
    Book(id="3", title="すすむ巨人", category="comics"),
    Book(id="4", title="DBおやじ", category="comics"),
    Book(id="5", title="週刊ダイヤモンド", category="magazine"),
    Book(id="6", title="ザ・社長", category="magazine"),    
]

def get_books_by_category(
    category: Optional[str] = None
    ) -> list[Book]:
    if category is None:
        return books
    else:
        return [book for book in books if book.category == category]