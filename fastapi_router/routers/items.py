from fastapi import APIRouter
from schemas.item import Item

router = APIRouter()

@router.get("/itmes/", response_model=dict)
async def read_itmes():
    return {"message": "アイテムを表示", "itmes": []}

@router.post("/itmes/", response_model=dict)
async def create_item(item: Item):
    return {"message": "アイテムを作成しました", "item": item}

@router.put("/itmes/", response_model=dict)
async def update_item(item_id: int, item: Item):
    return {"message": "アイテムを更新しました", "item_id": item_id, "item": item}

@router.delete("/itmes/", response_model=dict)
async def delete_item(item_id: int):
    return {"message": "アイテムを削除しました", "item_id": item_id}