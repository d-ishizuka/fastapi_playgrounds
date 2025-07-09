import asyncio
import time
import threading
from concurrent.futures import ThreadPoolExecutor
from sqlalchemy import create_engine, Column, Integer, String, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)

# 同期用の設定
sync_engine = create_engine('sqlite:///sync_example.sqlite', echo=False)
SyncSession = sessionmaker(bind=sync_engine)

# 非同期用の設定
async_engine = create_async_engine('sqlite+aiosqlite:///async_example.sqlite', echo=False)
async_session = async_sessionmaker(bind=async_engine, class_=AsyncSession)

def simulate_slow_db_operation_sync():
    """同期処理で遅いDB操作をシミュレート"""
    time.sleep(0.1)  # 100msの遅延をシミュレート
    return "同期処理完了"

async def simulate_slow_db_operation_async():
    """非同期処理で遅いDB操作をシミュレート"""
    await asyncio.sleep(0.1)  # 100msの遅延をシミュレート
    return "非同期処理完了"

def demonstrate_sync_sequential():
    """同期処理の逐次実行"""
    print("=== 同期処理の逐次実行 ===")
    start_time = time.time()
    
    results = []
    for i in range(3):
        result = simulate_slow_db_operation_sync()
        results.append(result)
    
    end_time = time.time()
    print(f"実行時間: {end_time - start_time:.3f}秒")
    print(f"結果: {results}")
    print()

def demonstrate_sync_parallel():
    """同期処理の並行実行（スレッド使用）"""
    print("=== 同期処理の並行実行（スレッド使用） ===")
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(simulate_slow_db_operation_sync) for _ in range(3)]
        results = [future.result() for future in futures]
    
    end_time = time.time()
    print(f"実行時間: {end_time - start_time:.3f}秒")
    print(f"結果: {results}")
    print()

async def demonstrate_async_sequential():
    """非同期処理の逐次実行"""
    print("=== 非同期処理の逐次実行 ===")
    start_time = time.time()
    
    results = []
    for i in range(3):
        result = await simulate_slow_db_operation_async()
        results.append(result)
    
    end_time = time.time()
    print(f"実行時間: {end_time - start_time:.3f}秒")
    print(f"結果: {results}")
    print()

async def demonstrate_async_parallel():
    """非同期処理の並行実行"""
    print("=== 非同期処理の並行実行 ===")
    start_time = time.time()
    
    tasks = [simulate_slow_db_operation_async() for _ in range(3)]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"実行時間: {end_time - start_time:.3f}秒")
    print(f"結果: {results}")
    print()

async def demonstrate_real_db_operations():
    """実際のDB操作での比較"""
    print("=== 実際のDB操作での比較 ===")
    
    # 非同期DB操作の例
    async def async_db_operations():
        async with async_session() as session:
            # 複数のクエリを並行実行
            tasks = [
                session.execute(select(User).where(User.id == 1)),
                session.execute(select(User).where(User.id == 2)),
                session.execute(select(User).where(User.id == 3))
            ]
            results = await asyncio.gather(*tasks)
            return [result.scalar_one_or_none() for result in results]
    
    start_time = time.time()
    users = await async_db_operations()
    end_time = time.time()
    
    print(f"非同期DB操作時間: {end_time - start_time:.3f}秒")
    print(f"取得したユーザー数: {len([u for u in users if u is not None])}")
    print()

def explain_key_differences():
    """重要な違いの説明"""
    print("=== 重要な違いの説明 ===")
    print("1. スレッドブロッキング:")
    print("   - 同期処理: DB操作中はスレッドがブロックされ、他の処理ができない")
    print("   - 非同期処理: DB操作中も他の非同期処理を並行実行できる")
    print()
    
    print("2. リソース効率:")
    print("   - 同期処理: 各DB操作に1つのスレッドが必要")
    print("   - 非同期処理: 1つのスレッドで複数のDB操作を処理可能")
    print()
    
    print("3. スケーラビリティ:")
    print("   - 同期処理: スレッド数の制限により同時接続数に制限")
    print("   - 非同期処理: より多くの同時接続を効率的に処理可能")
    print()
    
    print("4. 複雑性:")
    print("   - 同期処理: シンプルで理解しやすい")
    print("   - 非同期処理: async/awaitの概念理解が必要")
    print()

async def main():
    """メイン実行関数"""
    # 同期処理のデモ
    demonstrate_sync_sequential()
    demonstrate_sync_parallel()
    
    # 非同期処理のデモ
    await demonstrate_async_sequential()
    await demonstrate_async_parallel()
    
    # 説明
    explain_key_differences()

if __name__ == "__main__":
    asyncio.run(main()) 