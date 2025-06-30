from fastapi import FastAPI
import asyncio
import httpx

app = FastAPI()

async def fetch_address(zip_code: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={zip_code}"
        )
    return response.json()

@app.get("/addresses/")
async def get_addresses():
    zip_codes = [
        '0600000', #北海道
        '1000001', #東京
        '9000000', #沖縄
    ]
    return await asyncio.gather(*(fetch_address(zip_code) for zip_code in zip_codes))