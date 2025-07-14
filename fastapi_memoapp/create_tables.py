import asyncio
from db import engine, Base
from models.memo import Memo

async def create_tables():
    """データベースのテーブルを作成する関数"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    print("テーブルが正常に作成されました！")

if __name__ == "__main__":
    asyncio.run(create_tables()) 