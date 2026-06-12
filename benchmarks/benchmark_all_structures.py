import time
import sys
import gc
from pathlib import Path

# Add project root to path to run directly from development folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pythonstl import stack, queue, vector, stl_set, stl_map, priority_queue
from pythonstl.facade.stack import RUST_AVAILABLE as STACK_RUST_AVAILABLE
from pythonstl.facade.queue import RUST_AVAILABLE as QUEUE_RUST_AVAILABLE
from pythonstl.facade.vector import RUST_AVAILABLE as VECTOR_RUST_AVAILABLE
from pythonstl.facade.set import RUST_AVAILABLE as SET_RUST_AVAILABLE
from pythonstl.facade.map import RUST_AVAILABLE as MAP_RUST_AVAILABLE
from pythonstl.facade.priority_queue import RUST_AVAILABLE as PQ_RUST_AVAILABLE

def run_benchmark(name, py_func, rust_func, has_rust):
    print(f"Benchmarking {name}...")
    
    # Run Python benchmark
    gc.collect()
    start = time.perf_counter()
    py_func()
    py_time = time.perf_counter() - start
    
    rust_time = None
    if has_rust:
        gc.collect()
        start = time.perf_counter()
        rust_func()
        rust_time = time.perf_counter() - start
        
    return py_time, rust_time

# ----------------- Benchmark Workloads -----------------

def bench_stack_py():
    s = stack(use_rust=False)
    for i in range(500000):
        s.push(i)
    for _ in range(500000):
        s.pop()

def bench_stack_rust():
    s = stack(use_rust=True)
    for i in range(500000):
        s.push(i)
    for _ in range(500000):
        s.pop()

def bench_queue_py():
    q = queue(use_rust=False)
    for i in range(500000):
        q.push(i)
    for _ in range(500000):
        q.pop()

def bench_queue_rust():
    q = queue(use_rust=True)
    for i in range(500000):
        q.push(i)
    for _ in range(500000):
        q.pop()

def bench_vector_py():
    v = vector(use_rust=False)
    # 1. Push back 10,000 items
    for i in range(10000):
        v.push_back(i)
    # 2. Access via at()
    for i in range(10000):
        _ = v.at(i)
    # 3. In-place insertions
    for i in range(100):
        v.insert(5000, i)

def bench_vector_rust():
    v = vector(use_rust=True)
    # 1. Push back 10,000 items
    for i in range(10000):
        v.push_back(i)
    # 2. Access via at()
    for i in range(10000):
        _ = v.at(i)
    # 3. In-place insertions
    for i in range(100):
        v.insert(5000, i)

def bench_set_py():
    s = stl_set(use_rust=False)
    # 1. Insertions (50,000)
    for i in range(50000):
        s.insert(i)
    # 2. Lookup/Find (50,000)
    for i in range(50000):
        _ = s.find(i)
    # 3. Erasures (50,000)
    for i in range(50000):
        s.erase(i)

def bench_set_rust():
    s = stl_set(use_rust=True)
    # 1. Insertions (50,000)
    for i in range(50000):
        s.insert(i)
    # 2. Lookup/Find (50,000)
    for i in range(50000):
        _ = s.find(i)
    # 3. Erasures (50,000)
    for i in range(50000):
        s.erase(i)

def bench_map_py():
    m = stl_map(use_rust=False)
    # 1. Insertions (50,000)
    for i in range(50000):
        m.insert(i, i * 2)
    # 2. Lookup/Find (50,000)
    for i in range(50000):
        _ = m.find(i)
    # 3. Access via at()
    for i in range(50000):
        _ = m.at(i)
    # 4. Erasures (50,000)
    for i in range(50000):
        m.erase(i)

def bench_map_rust():
    m = stl_map(use_rust=True)
    # 1. Insertions (50,000)
    for i in range(50000):
        m.insert(i, i * 2)
    # 2. Lookup/Find (50,000)
    for i in range(50000):
        _ = m.find(i)
    # 3. Access via at()
    for i in range(50000):
        _ = m.at(i)
    # 4. Erasures (50,000)
    for i in range(50000):
        m.erase(i)

def bench_priority_queue_py():
    pq = priority_queue(use_rust=False)
    # 1. Pushes (50,000)
    for i in range(50000):
        pq.push(i)
    # 2. Pops (50,000)
    for _ in range(50000):
        _ = pq.top()
        pq.pop()

def bench_priority_queue_rust():
    pq = priority_queue(use_rust=True)
    # 1. Pushes (50,000)
    for i in range(50000):
        pq.push(i)
    # 2. Pops (50,000)
    for _ in range(50000):
        _ = pq.top()
        pq.pop()


# ----------------- Main Execution -----------------

def main():
    print("=============================================================")
    print("      PythonSTL Comprehensive Container Benchmark Suite      ")
    print("=============================================================\n")
    
    results = {}
    
    # 1. Stack
    py_t, rust_t = run_benchmark("Stack (500,000 cycles)", bench_stack_py, bench_stack_rust, STACK_RUST_AVAILABLE)
    results["Stack"] = (py_t, rust_t, STACK_RUST_AVAILABLE)
    
    # 2. Queue
    py_t, rust_t = run_benchmark("Queue (500,000 cycles)", bench_queue_py, bench_queue_rust, QUEUE_RUST_AVAILABLE)
    results["Queue"] = (py_t, rust_t, QUEUE_RUST_AVAILABLE)
    
    # 3. Vector
    py_t, rust_t = run_benchmark("Vector (10,000 push/access + 100 inserts)", bench_vector_py, bench_vector_rust, VECTOR_RUST_AVAILABLE)
    results["Vector"] = (py_t, rust_t, VECTOR_RUST_AVAILABLE)
    
    # 4. Set
    py_t, rust_t = run_benchmark("Set (50,000 inserts/finds/erases)", bench_set_py, bench_set_rust, SET_RUST_AVAILABLE)
    results["Set"] = (py_t, rust_t, SET_RUST_AVAILABLE)
    
    # 5. Map
    py_t, rust_t = run_benchmark("Map (50,000 inserts/finds/ats/erases)", bench_map_py, bench_map_rust, MAP_RUST_AVAILABLE)
    results["Map"] = (py_t, rust_t, MAP_RUST_AVAILABLE)
    
    # 6. Priority Queue
    py_t, rust_t = run_benchmark("Priority Queue (50,000 push/pops)", bench_priority_queue_py, bench_priority_queue_rust, PQ_RUST_AVAILABLE)
    results["Priority Queue"] = (py_t, rust_t, PQ_RUST_AVAILABLE)
    
    print("\n" + "=" * 70)
    print("                    PERFORMANCE SUMMARY TABLE                ")
    print("=" * 70)
    print(f"{'Container Class':<18} | {'Pure Python':<12} | {'Python + Rust':<15} | {'Speedup Status':<18}")
    print("-" * 70)
    
    for container, (py_time, rust_time, is_rust) in results.items():
        py_str = f"{py_time:.4f}s"
        if is_rust and rust_time is not None:
            rust_str = f"{rust_time:.4f}s"
            speedup = py_time / rust_time
            status = f"{speedup:.2f}x faster"
        else:
            rust_str = "N/A"
            status = "Pure Py Fallback"
            
        print(f"{container:<18} | {py_str:<12} | {rust_str:<15} | {status:<18}")
        
    print("=============================================================")
    print("Note: Containers marked 'Pure Py Fallback' will run using the")
    print("original python backends until their Rust cores are built.")
    print("=============================================================")

if __name__ == "__main__":
    main()
