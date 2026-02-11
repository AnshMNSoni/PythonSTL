"""
Benchmark for vector operations.

Compares pystl.vector performance against Python's built-in list.
"""

import timeit
from pythonstl import vector


def benchmark_pystl_vector_push_back():
    """Benchmark push_back operations on pystl.vector."""
    v = vector()
    for i in range(10000):
        v.push_back(i)


def benchmark_list_append():
    """Benchmark append operations on Python list."""
    lst = []
    for i in range(10000):
        lst.append(i)


def benchmark_pystl_vector_insert():
    """Benchmark insert operations on pystl.vector."""
    v = vector()
    for i in range(1000):
        v.push_back(i)
    for i in range(100):
        v.insert(500, i)


def benchmark_list_insert():
    """Benchmark insert operations on Python list."""
    lst = list(range(1000))
    for i in range(100):
        lst.insert(500, i)


def benchmark_pystl_vector_at():
    """Benchmark random access on pystl.vector."""
    v = vector()
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
    print("=" * 60)
    print("Vector Benchmark: pystl.vector vs Python list")
    print("=" * 60)
    print()
    
    # Push back/Append benchmark
    print("Push Back/Append Operations (10,000 elements):")
    print("-" * 60)
    
    pystl_push_time = timeit.timeit(benchmark_pystl_vector_push_back, number=100)
    list_append_time = timeit.timeit(benchmark_list_append, number=100)
    
    print(f"pystl.vector.push_back():  {pystl_push_time:.4f} seconds")
    print(f"list.append():             {list_append_time:.4f} seconds")
    print(f"Ratio (pystl/list):        {pystl_push_time/list_append_time:.2f}x")
    print()
    
    # Insert benchmark
    print("Insert Operations (100 inserts into 1,000 elements):")
    print("-" * 60)
    
    pystl_insert_time = timeit.timeit(benchmark_pystl_vector_insert, number=100)
    list_insert_time = timeit.timeit(benchmark_list_insert, number=100)
    
    print(f"pystl.vector.insert():     {pystl_insert_time:.4f} seconds")
    print(f"list.insert():             {list_insert_time:.4f} seconds")
    print(f"Ratio (pystl/list):        {pystl_insert_time/list_insert_time:.2f}x")
    print()
    
    # Random access benchmark
    print("Random Access (10,000 accesses):")
    print("-" * 60)
    
    pystl_at_time = timeit.timeit(benchmark_pystl_vector_at, number=100)
    list_index_time = timeit.timeit(benchmark_list_indexing, number=100)
    
    print(f"pystl.vector.at():         {pystl_at_time:.4f} seconds")
    print(f"list[i]:                   {list_index_time:.4f} seconds")
    print(f"Ratio (pystl/list):        {pystl_at_time/list_index_time:.2f}x")
    print()
    
    print("=" * 60)
    print("Note: pystl.vector wraps Python list with bounds checking.")
    print("The at() method adds safety at a small performance cost.")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
