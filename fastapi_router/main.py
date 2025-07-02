from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Category(BaseModel):
    category_id: int
    category_name: str


class Item(BaseModel):
    item_id: int
    item_name: str
    category_id: int

@app.get("/categories/", response_model=dict)
async def read_categories():
    return {"message": "カテゴリを表示", "categories": []}

@app.post("/categories/", response_model=dict)
async def create_category(category: Category):
    return {"message": "カテゴリを作成しました", "category": category}

@app.put("/categories/", response_model=dict)
async def update_category(category_id: int, category: Category):
    return {"message": "カテゴリを更新しました", "category_id": category_id, "category": category}

@app.delete("/categories/", response_model=dict)
async def delete_category(category_id: int):
    return {"message": "カテゴリを削除しました", "category_id": category_id}

@app.get("/itmes/", response_model=dict)
async def read_itmes():
    return {"message": "アイテムを表示", "itmes": []}

@app.post("/itmes/", response_model=dict)
async def create_item(item: Item):
    return {"message": "アイテムを作成しました", "item": item}

@app.put("/itmes/", response_model=dict)
async def update_item(item_id: int, item: Item):
    return {"message": "アイテムを更新しました", "item_id": item_id, "item": item}

@app.delete("/itmes/", response_model=dict)
async def delete_item(item_id: int):
    return {"message": "アイテムを削除しました", "item_id": item_id}