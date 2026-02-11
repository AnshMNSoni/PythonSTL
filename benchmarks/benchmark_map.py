"""
Benchmark for map operations.

Compares pystl.stl_map performance against Python's built-in dict.
"""

import timeit
from pythonstl import stl_map


def benchmark_pystl_map_insert():
    """Benchmark insert operations on pystl.stl_map."""
    m = stl_map()
    for i in range(10000):
        m.insert(f"key_{i}", i)


def benchmark_dict_insert():
    """Benchmark insert operations on Python dict."""
    d = {}
    for i in range(10000):
        d[f"key_{i}"] = i


def benchmark_pystl_map_find():
    """Benchmark find operations on pystl.stl_map."""
    m = stl_map()
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


def benchmark_pystl_map_at():
    """Benchmark at() operations on pystl.stl_map."""
    m = stl_map()
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
    print("=" * 60)
    print("Map Benchmark: pystl.stl_map vs Python dict")
    print("=" * 60)
    print()
    
    # Insert benchmark
    print("Insert Operations (10,000 key-value pairs):")
    print("-" * 60)
    
    pystl_insert_time = timeit.timeit(benchmark_pystl_map_insert, number=100)
    dict_insert_time = timeit.timeit(benchmark_dict_insert, number=100)
    
    print(f"pystl.stl_map.insert():    {pystl_insert_time:.4f} seconds")
    print(f"dict[key] = value:         {dict_insert_time:.4f} seconds")
    print(f"Ratio (pystl/dict):        {pystl_insert_time/dict_insert_time:.2f}x")
    print()
    
    # Find benchmark
    print("Find/Contains Operations (10,000 lookups):")
    print("-" * 60)
    
    pystl_find_time = timeit.timeit(benchmark_pystl_map_find, number=100)
    dict_in_time = timeit.timeit(benchmark_dict_in, number=100)
    
    print(f"pystl.stl_map.find():      {pystl_find_time:.4f} seconds")
    print(f"key in dict:               {dict_in_time:.4f} seconds")
    print(f"Ratio (pystl/dict):        {pystl_find_time/dict_in_time:.2f}x")
    print()
    
    # Access benchmark
    print("Access Operations (10,000 accesses):")
    print("-" * 60)
    
    pystl_at_time = timeit.timeit(benchmark_pystl_map_at, number=100)
    dict_access_time = timeit.timeit(benchmark_dict_access, number=100)
    
    print(f"pystl.stl_map.at():        {pystl_at_time:.4f} seconds")
    print(f"dict[key]:                 {dict_access_time:.4f} seconds")
    print(f"Ratio (pystl/dict):        {pystl_at_time/dict_access_time:.2f}x")
    print()
    
    print("=" * 60)
    print("Note: pystl.stl_map wraps Python dict with STL-style API.")
    print("The facade pattern adds minimal overhead for type safety.")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
