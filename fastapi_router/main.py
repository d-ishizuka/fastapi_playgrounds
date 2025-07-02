from fastapi import FastAPI
from routers.categories import router as category_router
from routers.items import router as item_router

app = FastAPI()

app.include_router(category_router)
app.include_router(item_router)