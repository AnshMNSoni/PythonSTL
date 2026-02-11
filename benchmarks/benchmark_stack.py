"""
Benchmark for stack operations.

Compares pystl.stack performance against Python's built-in list.
"""

import timeit
from pythonstl import stack


def benchmark_pystl_stack_push():
    """Benchmark push operations on pystl.stack."""
    s = stack()
    for i in range(10000):
        s.push(i)


def benchmark_list_append():
    """Benchmark append operations on Python list."""
    lst = []
    for i in range(10000):
        lst.append(i)


def benchmark_pystl_stack_pop():
    """Benchmark pop operations on pystl.stack."""
    s = stack()
    for i in range(10000):
        s.push(i)
    for _ in range(10000):
        s.pop()


def benchmark_list_pop():
    """Benchmark pop operations on Python list."""
    lst = list(range(10000))
    for _ in range(10000):
        lst.pop()


def run_benchmarks():
    """Run all stack benchmarks and display results."""
    print("=" * 60)
    print("Stack Benchmark: pystl.stack vs Python list")
    print("=" * 60)
    print()
    
    # Push/Append benchmark
    print("Push/Append Operations (10,000 elements):")
    print("-" * 60)
    
    pystl_push_time = timeit.timeit(benchmark_pystl_stack_push, number=100)
    list_append_time = timeit.timeit(benchmark_list_append, number=100)
    
    print(f"pystl.stack.push():  {pystl_push_time:.4f} seconds")
    print(f"list.append():       {list_append_time:.4f} seconds")
    print(f"Ratio (pystl/list):  {pystl_push_time/list_append_time:.2f}x")
    print()
    
    # Pop benchmark
    print("Pop Operations (10,000 elements):")
    print("-" * 60)
    
    pystl_pop_time = timeit.timeit(benchmark_pystl_stack_pop, number=100)
    list_pop_time = timeit.timeit(benchmark_list_pop, number=100)
    
    print(f"pystl.stack.pop():   {pystl_pop_time:.4f} seconds")
    print(f"list.pop():          {list_pop_time:.4f} seconds")
    print(f"Ratio (pystl/list):  {pystl_pop_time/list_pop_time:.2f}x")
    print()
    
    print("=" * 60)
    print("Note: pystl.stack wraps Python list, so overhead is minimal.")
    print("The facade pattern adds a small constant-factor overhead.")
    print("=" * 60)


if __name__ == "__main__":
    run_benchmarks()
