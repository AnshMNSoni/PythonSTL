import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import timeit
from pythonstl import vector


def benchmark_pystl_rust_push_back():
    """Benchmark push_back operations on pystl.vector (Rust)."""
    v = vector(use_rust=True)
    for i in range(10000):
        v.push_back(i)


def benchmark_pystl_python_push_back():
    """Benchmark push_back operations on pystl.vector (Pure Python)."""
    v = vector(use_rust=False)
    for i in range(10000):
        v.push_back(i)


def benchmark_list_append():
    """Benchmark append operations on Python list."""
    lst = []
    for i in range(10000):
        lst.append(i)


def benchmark_pystl_rust_insert():
    """Benchmark insert operations on pystl.vector (Rust)."""
    v = vector(use_rust=True)
    for i in range(1000):
        v.push_back(i)
    for i in range(100):
        v.insert(500, i)


def benchmark_pystl_python_insert():
    """Benchmark insert operations on pystl.vector (Pure Python)."""
    v = vector(use_rust=False)
    for i in range(1000):
        v.push_back(i)
    for i in range(100):
        v.insert(500, i)


def benchmark_list_insert():
    """Benchmark insert operations on Python list."""
    lst = list(range(1000))
    for i in range(100):
        lst.insert(500, i)


def benchmark_pystl_rust_at():
    """Benchmark random access on pystl.vector (Rust)."""
    v = vector(use_rust=True)
    for i in range(10000):
        v.push_back(i)
    total = 0
    for i in range(10000):
        total += v.at(i)


def benchmark_pystl_python_at():
    """Benchmark random access on pystl.vector (Pure Python)."""
    v = vector(use_rust=False)
    for i in range(10000):
        v.push_back(i)
    total = 0
    for i in range(10000):
        total += v.at(i)


def benchmark_list_indexing():
    """Benchmark random access on Python list."""
    lst = list(range(10000))
    total = 0
    for i in range(10000):
        total += lst[i]


def run_benchmarks():
    """Run all vector benchmarks and display results."""
    print("=" * 75)
    print("Vector Benchmark: pystl.vector (Rust vs Python) vs Python list")
    print("=" * 75)
    print()
    
    # Push back/Append benchmark
    print("Push Back/Append Operations (10,000 elements):")
    print("-" * 75)
    
    rust_push_time = timeit.timeit(benchmark_pystl_rust_push_back, number=100)
    python_push_time = timeit.timeit(benchmark_pystl_python_push_back, number=100)
    list_append_time = timeit.timeit(benchmark_list_append, number=100)
    
    print(f"pystl.vector(use_rust=True).push_back():   {rust_push_time:.4f} seconds")
    print(f"pystl.vector(use_rust=False).push_back():  {python_push_time:.4f} seconds")
    print(f"list.append() [Native List]:               {list_append_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python:              {python_push_time/rust_push_time:.2f}x")
    print(f"Ratio (Rust/Native List):                  {rust_push_time/list_append_time:.2f}x")
    print()
    
    # Insert benchmark
    print("Insert Operations (100 inserts into 1,000 elements):")
    print("-" * 75)
    
    rust_insert_time = timeit.timeit(benchmark_pystl_rust_insert, number=100)
    python_insert_time = timeit.timeit(benchmark_pystl_python_insert, number=100)
    list_insert_time = timeit.timeit(benchmark_list_insert, number=100)
    
    print(f"pystl.vector(use_rust=True).insert():      {rust_insert_time:.4f} seconds")
    print(f"pystl.vector(use_rust=False).insert():     {python_insert_time:.4f} seconds")
    print(f"list.insert() [Native List]:               {list_insert_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python:              {python_insert_time/rust_insert_time:.2f}x")
    print(f"Ratio (Rust/Native List):                  {rust_insert_time/list_insert_time:.2f}x")
    print()
    
    # Random access benchmark
    print("Random Access (10,000 accesses):")
    print("-" * 75)
    
    rust_at_time = timeit.timeit(benchmark_pystl_rust_at, number=100)
    python_at_time = timeit.timeit(benchmark_pystl_python_at, number=100)
    list_index_time = timeit.timeit(benchmark_list_indexing, number=100)
    
    print(f"pystl.vector(use_rust=True).at():          {rust_at_time:.4f} seconds")
    print(f"pystl.vector(use_rust=False).at():         {python_at_time:.4f} seconds")
    print(f"list[i] [Native List]:                     {list_index_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python:              {python_at_time/rust_at_time:.2f}x")
    print(f"Ratio (Rust/Native List):                  {rust_at_time/list_index_time:.2f}x")
    print()
    
    print("=" * 75)
    print("Note: Native list is a direct C implementation in Python (no FFI).")
    print("Comparing Rust vector vs. Pure Python vector isolates the FFI/Rust library speedup.")
    print("=" * 75)


if __name__ == "__main__":
    run_benchmarks()
