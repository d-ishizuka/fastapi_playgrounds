import time

# 同期処理
def sync_task(name):
    print(f"{name} タスク開始")
    time.sleep(2)
    print(f"{name} タスク終了")

def run_sync_tasks():
    sync_task("タスク1")
    sync_task("タスク2")
    sync_task("タスク3")

print("同期処理の例：")
run_sync_tasks()

# 非同期処理
import asyncio

async def async_task(name):
    print(f"{name} タスク開始")
    await asyncio.sleep(2)
    print(f"{name} タスク終了")

async def run_async_tasks():
    await asyncio.gather(
        async_task("タスクA"),
        async_task("タスクB"),
        async_task("タスクC")
    )

print("非同期処理の例：")
asyncio.run(run_async_tasks())