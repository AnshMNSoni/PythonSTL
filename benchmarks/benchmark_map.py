import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import timeit
from pythonstl import stl_map


def benchmark_pystl_rust_map_insert():
    """Benchmark insert operations on pystl.stl_map (Rust)."""
    m = stl_map(use_rust=True)
    for i in range(10000):
        m.insert(f"key_{i}", i)


def benchmark_pystl_python_map_insert():
    """Benchmark insert operations on pystl.stl_map (Pure Python AVL tree)."""
    m = stl_map(use_rust=False)
    for i in range(10000):
        m.insert(f"key_{i}", i)


def benchmark_dict_insert():
    """Benchmark insert operations on Python dict."""
    d = {}
    for i in range(10000):
        d[f"key_{i}"] = i


def benchmark_pystl_rust_map_find():
    """Benchmark find operations on pystl.stl_map (Rust)."""
    m = stl_map(use_rust=True)
    for i in range(10000):
        m.insert(f"key_{i}", i)
    count = 0
    for i in range(10000):
        if m.find(f"key_{i}"):
            count += 1


def benchmark_pystl_python_map_find():
    """Benchmark find operations on pystl.stl_map (Pure Python AVL tree)."""
    m = stl_map(use_rust=False)
    for i in range(10000):
        m.insert(f"key_{i}", i)
    count = 0
    for i in range(10000):
        if m.find(f"key_{i}"):
            count += 1


def benchmark_dict_in():
    """Benchmark 'in' operations on Python dict."""
    d = {f"key_{i}": i for i in range(10000)}
    count = 0
    for i in range(10000):
        if f"key_{i}" in d:
            count += 1


def benchmark_pystl_rust_map_at():
    """Benchmark at() operations on pystl.stl_map (Rust)."""
    m = stl_map(use_rust=True)
    for i in range(10000):
        m.insert(f"key_{i}", i)
    total = 0
    for i in range(10000):
        total += m.at(f"key_{i}")


def benchmark_pystl_python_map_at():
    """Benchmark at() operations on pystl.stl_map (Pure Python AVL tree)."""
    m = stl_map(use_rust=False)
    for i in range(10000):
        m.insert(f"key_{i}", i)
    total = 0
    for i in range(10000):
        total += m.at(f"key_{i}")


def benchmark_dict_access():
    """Benchmark access operations on Python dict."""
    d = {f"key_{i}": i for i in range(10000)}
    total = 0
    for i in range(10000):
        total += d[f"key_{i}"]


def run_benchmarks():
    """Run all map benchmarks and display results."""
    print("=" * 80)
    print("Map Benchmark: pystl.stl_map (Rust B-Tree vs Python AVL) vs Python dict (Hash)")
    print("=" * 80)
    print()
    
    # Insert benchmark
    print("Insert Operations (10,000 key-value pairs):")
    print("-" * 80)
    
    rust_insert_time = timeit.timeit(benchmark_pystl_rust_map_insert, number=10)
    python_insert_time = timeit.timeit(benchmark_pystl_python_map_insert, number=10)
    dict_insert_time = timeit.timeit(benchmark_dict_insert, number=10)
    
    print(f"pystl.stl_map(use_rust=True).insert():    {rust_insert_time:.4f} seconds")
    print(f"pystl.stl_map(use_rust=False).insert():   {python_insert_time:.4f} seconds")
    print(f"dict[key] = value [Unordered Hash]:       {dict_insert_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python AVL:         {python_insert_time/rust_insert_time:.2f}x")
    print(f"Ratio (Rust vs. Unordered Hash):          {rust_insert_time/dict_insert_time:.2f}x")
    print()
    
    # Find benchmark
    print("Find/Contains Operations (10,000 lookups):")
    print("-" * 80)
    
    rust_find_time = timeit.timeit(benchmark_pystl_rust_map_find, number=10)
    python_find_time = timeit.timeit(benchmark_pystl_python_map_find, number=10)
    dict_in_time = timeit.timeit(benchmark_dict_in, number=10)
    
    print(f"pystl.stl_map(use_rust=True).find():      {rust_find_time:.4f} seconds")
    print(f"pystl.stl_map(use_rust=False).find():     {python_find_time:.4f} seconds")
    print(f"key in dict [Unordered Hash]:             {dict_in_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python AVL:         {python_find_time/rust_find_time:.2f}x")
    print(f"Ratio (Rust vs. Unordered Hash):          {rust_find_time/dict_in_time:.2f}x")
    print()
    
    # Access benchmark
    print("Access Operations (10,000 accesses):")
    print("-" * 80)
    
    rust_at_time = timeit.timeit(benchmark_pystl_rust_map_at, number=10)
    python_at_time = timeit.timeit(benchmark_pystl_python_map_at, number=10)
    dict_access_time = timeit.timeit(benchmark_dict_access, number=10)
    
    print(f"pystl.stl_map(use_rust=True).at():        {rust_at_time:.4f} seconds")
    print(f"pystl.stl_map(use_rust=False).at():       {python_at_time:.4f} seconds")
    print(f"dict[key] [Unordered Hash]:               {dict_access_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python AVL:         {python_at_time/rust_at_time:.2f}x")
    print(f"Ratio (Rust vs. Unordered Hash):          {rust_at_time/dict_access_time:.2f}x")
    print()
    
    print("=" * 80)
    print("Note: Python's dict is an unordered hash table ($O(1)$ lookup/insert).")
    print("PySTL's stl_map is a sorted tree container ($O(log N)$ lookup/insert).")
    print("Comparing Rust map vs. Pure Python map isolates the actual FFI/Rust library speedup.")
    print("=" * 80)


if __name__ == "__main__":
    run_benchmarks()
