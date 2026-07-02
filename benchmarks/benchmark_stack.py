import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

import timeit
from pythonstl import stack


def benchmark_pystl_rust_push():
    """Benchmark push operations on pystl.stack (Rust)."""
    s = stack(use_rust=True)
    for i in range(10000):
        s.push(i)


def benchmark_pystl_python_push():
    """Benchmark push operations on pystl.stack (Pure Python)."""
    s = stack(use_rust=False)
    for i in range(10000):
        s.push(i)


def benchmark_list_append():
    """Benchmark append operations on Python list."""
    lst = []
    for i in range(10000):
        lst.append(i)


def benchmark_pystl_rust_pop():
    """Benchmark pop operations on pystl.stack (Rust)."""
    s = stack(use_rust=True)
    for i in range(10000):
        s.push(i)
    for _ in range(10000):
        s.pop()


def benchmark_pystl_python_pop():
    """Benchmark pop operations on pystl.stack (Pure Python)."""
    s = stack(use_rust=False)
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
    print("=" * 70)
    print("Stack Benchmark: pystl.stack (Rust vs Python) vs Python list")
    print("=" * 70)
    print()
    
    # Push/Append benchmark
    print("Push/Append Operations (10,000 elements):")
    print("-" * 70)
    
    rust_push_time = timeit.timeit(benchmark_pystl_rust_push, number=100)
    python_push_time = timeit.timeit(benchmark_pystl_python_push, number=100)
    list_append_time = timeit.timeit(benchmark_list_append, number=100)
    
    print(f"pystl.stack(use_rust=True).push():   {rust_push_time:.4f} seconds")
    print(f"pystl.stack(use_rust=False).push():  {python_push_time:.4f} seconds")
    print(f"list.append() [Native List]:         {list_append_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python:        {python_push_time/rust_push_time:.2f}x")
    print(f"Ratio (Rust/Native List):            {rust_push_time/list_append_time:.2f}x")
    print()
    
    # Pop benchmark
    print("Pop Operations (10,000 elements):")
    print("-" * 70)
    
    rust_pop_time = timeit.timeit(benchmark_pystl_rust_pop, number=100)
    python_pop_time = timeit.timeit(benchmark_pystl_python_pop, number=100)
    list_pop_time = timeit.timeit(benchmark_list_pop, number=100)
    
    print(f"pystl.stack(use_rust=True).pop():    {rust_pop_time:.4f} seconds")
    print(f"pystl.stack(use_rust=False).pop():   {python_pop_time:.4f} seconds")
    print(f"list.pop() [Native List]:            {list_pop_time:.4f} seconds")
    print(f"Rust Speedup vs. Pure Python:        {python_pop_time/rust_pop_time:.2f}x")
    print(f"Ratio (Rust/Native List):            {rust_pop_time/list_pop_time:.2f}x")
    print()
    
    print("=" * 70)
    print("Note: Native list is a direct C implementation in Python (no FFI).")
    print("Comparing Rust stack vs. Pure Python stack isolates the FFI/Rust library speedup.")
    print("=" * 70)


if __name__ == "__main__":
    run_benchmarks()
