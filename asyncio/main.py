import asyncio

async def fetch_data():
    print("データ取得を開始します...")
    await asyncio.sleep(4)
    print("データが取得されました!!!!「data:xyz」")

async def perform_calculation():
    print("計算を開始します...")
    await asyncio.sleep(2)
    print("計算が完了しました!!!答え「12345」")

async def main():
    print("データ取得と計算を開始する前")
    await asyncio.gather(fetch_data(), perform_calculation())
    print("すべてのタスクが完了しました")

asyncio.run(main())