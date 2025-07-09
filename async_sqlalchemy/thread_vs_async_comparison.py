import asyncio
import time
import threading
from concurrent.futures import ThreadPoolExecutor
import os

def simulate_io_bound_operation_sync():
    """I/O待機をシミュレートする同期処理"""
    time.sleep(0.1)  # ファイル読み込みやDBアクセスをシミュレート
    return f"同期処理完了 (スレッド: {threading.current_thread().name})"

async def simulate_io_bound_operation_async():
    """I/O待機をシミュレートする非同期処理"""
    await asyncio.sleep(0.1)  # ファイル読み込みやDBアクセスをシミュレート
    return f"非同期処理完了 (スレッド: {threading.current_thread().name})"

def simulate_cpu_bound_operation():
    """CPU負荷の高い処理をシミュレート"""
    result = 0
    for i in range(1000000):
        result += i * i
    return f"CPU処理完了: {result} (スレッド: {threading.current_thread().name})"

async def demonstrate_threading():
    """マルチスレッド処理の詳細"""
    print("=== マルチスレッド処理の詳細 ===")
    print(f"メインスレッド: {threading.current_thread().name}")
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(simulate_io_bound_operation_sync) for _ in range(3)]
        results = [future.result() for future in futures]
    
    end_time = time.time()
    print(f"実行時間: {end_time - start_time:.3f}秒")
    for result in results:
        print(f"  {result}")
    print()

async def demonstrate_async():
    """非同期処理の詳細"""
    print("=== 非同期処理の詳細 ===")
    print(f"メインスレッド: {threading.current_thread().name}")
    
    start_time = time.time()
    
    tasks = [simulate_io_bound_operation_async() for _ in range(3)]
    results = await asyncio.gather(*tasks)
    
    end_time = time.time()
    print(f"実行時間: {end_time - start_time:.3f}秒")
    for result in results:
        print(f"  {result}")
    print()

async def demonstrate_cpu_bound_comparison():
    """CPU負荷処理での比較"""
    print("=== CPU負荷処理での比較 ===")
    
    # マルチスレッドでのCPU負荷処理
    print("マルチスレッドでのCPU負荷処理:")
    start_time = time.time()
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(simulate_cpu_bound_operation) for _ in range(3)]
        results = [future.result() for future in futures]
    end_time = time.time()
    print(f"実行時間: {end_time - start_time:.3f}秒")
    for result in results:
        print(f"  {result}")
    print()
    
    # 非同期でのCPU負荷処理（実際には並行しない）
    print("非同期でのCPU負荷処理（逐次実行）:")
    async def cpu_bound_async():
        start_time = time.time()
        results = []
        for i in range(3):
            # CPU負荷処理は非同期でも逐次実行される
            result = await asyncio.to_thread(simulate_cpu_bound_operation)
            results.append(result)
        end_time = time.time()
        print(f"実行時間: {end_time - start_time:.3f}秒")
        for result in results:
            print(f"  {result}")
    
    await cpu_bound_async()
    print()

def explain_key_differences():
    """重要な違いの説明"""
    print("=== マルチスレッド vs 非同期処理の違い ===")
    print()
    
    print("1. スレッドの使用:")
    print("   - マルチスレッド: 複数のスレッドを実際に作成・管理")
    print("   - 非同期処理: 1つのスレッドで複数のタスクを切り替え")
    print()
    
    print("2. 適している処理:")
    print("   - マルチスレッド: CPU負荷の高い処理、並列計算")
    print("   - 非同期処理: I/O待機の多い処理（DB、ネットワーク、ファイル）")
    print()
    
    print("3. リソース消費:")
    print("   - マルチスレッド: 各スレッドにメモリオーバーヘッド（約1MB/スレッド）")
    print("   - 非同期処理: 軽量なタスク切り替え、メモリ効率が良い")
    print()
    
    print("4. スケーラビリティ:")
    print("   - マルチスレッド: スレッド数の制限（通常数百〜数千）")
    print("   - 非同期処理: 数万〜数十万のタスクを同時処理可能")
    print()
    
    print("5. デバッグの複雑さ:")
    print("   - マルチスレッド: 競合状態、デッドロック、スレッド間通信")
    print("   - 非同期処理: シングルスレッドなので競合状態が少ない")
    print()
    
    print("6. 実際の使用例:")
    print("   - マルチスレッド: 画像処理、機械学習、数値計算")
    print("   - 非同期処理: Webサーバー、API、データベース操作")
    print()

async def demonstrate_mixed_operations():
    """混在する処理での比較"""
    print("=== 混在する処理での比較 ===")
    
    async def mixed_async_operations():
        """非同期処理でI/OとCPU処理を混在"""
        print("非同期処理（I/O + CPU）:")
        start_time = time.time()
        
        # I/O処理は並行実行
        io_tasks = [simulate_io_bound_operation_async() for _ in range(3)]
        
        # CPU処理は別スレッドで実行
        cpu_tasks = [asyncio.to_thread(simulate_cpu_bound_operation) for _ in range(2)]
        
        # 全て並行実行
        all_tasks = io_tasks + cpu_tasks
        results = await asyncio.gather(*all_tasks)
        
        end_time = time.time()
        print(f"実行時間: {end_time - start_time:.3f}秒")
        for result in results:
            print(f"  {result}")
        print()
    
    await mixed_async_operations()

async def main():
    """メイン実行関数"""
    await demonstrate_threading()
    await demonstrate_async()
    await demonstrate_cpu_bound_comparison()
    await demonstrate_mixed_operations()
    explain_key_differences()

if __name__ == "__main__":
    asyncio.run(main()) 