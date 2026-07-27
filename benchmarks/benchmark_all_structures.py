"""
Performance benchmark comparing C++ (Rust backend), Pure Python, and Native Python built-in data structures.
"""

import time
import sys
import gc
import heapq
from collections import deque
from pathlib import Path

# Add project root to path to run directly from development folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pythonstl import stack, queue, vector, stl_set, stl_map, priority_queue
from pythonstl.containers.stack import RUST_AVAILABLE as STACK_RUST_AVAILABLE
from pythonstl.containers.queue import RUST_AVAILABLE as QUEUE_RUST_AVAILABLE
from pythonstl.containers.vector import RUST_AVAILABLE as VECTOR_RUST_AVAILABLE
from pythonstl.containers.set import RUST_AVAILABLE as SET_RUST_AVAILABLE
from pythonstl.containers.map import RUST_AVAILABLE as MAP_RUST_AVAILABLE
from pythonstl.containers.priority_queue import RUST_AVAILABLE as PQ_RUST_AVAILABLE


def run_benchmark(name, py_func, rust_func, has_rust, native_func):
    print(f"Benchmarking {name}...")
    
    # 1. Run Pure Python benchmark
    gc.collect()
    start = time.perf_counter()
    py_func()
    py_time = time.perf_counter() - start
    
    # 2. Run Rust benchmark
    rust_time = None
    if has_rust:
        gc.collect()
        start = time.perf_counter()
        rust_func()
        rust_time = time.perf_counter() - start
        
    # 3. Run Native Python built-in benchmark
    gc.collect()
    start = time.perf_counter()
    native_func()
    native_time = time.perf_counter() - start
        
    return py_time, rust_time, native_time


# ==========================================
# 1. STACK WORKLOADS
# ==========================================
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


def bench_stack_native():
    s = []
    for i in range(500000):
        s.append(i)
    for _ in range(500000):
        s.pop()


# ==========================================
# 2. QUEUE WORKLOADS
# ==========================================
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


def bench_queue_native():
    q = deque()
    for i in range(500000):
        q.append(i)
    for _ in range(500000):
        q.popleft()


# ==========================================
# 3. VECTOR WORKLOADS
# ==========================================
def bench_vector_py():
    v = vector(use_rust=False)
    for i in range(10000):
        v.push_back(i)
    for i in range(10000):
        _ = v.at(i)
    for i in range(100):
        v.insert(5000, i)


def bench_vector_rust():
    v = vector(use_rust=True)
    for i in range(10000):
        v.push_back(i)
    for i in range(10000):
        _ = v.at(i)
    for i in range(100):
        v.insert(5000, i)


def bench_vector_native():
    v = []
    for i in range(10000):
        v.append(i)
    for i in range(10000):
        _ = v[i]
    for i in range(100):
        v.insert(5000, i)


# ==========================================
# 4. SET WORKLOADS
# ==========================================
def bench_set_py():
    s = stl_set(use_rust=False)
    for i in range(10000):
        s.insert(i)
    for i in range(10000):
        _ = s.find(i)
    for i in range(10000):
        s.erase(i)


def bench_set_rust():
    s = stl_set(use_rust=True)
    for i in range(10000):
        s.insert(i)
    for i in range(10000):
        _ = s.find(i)
    for i in range(10000):
        s.erase(i)


def bench_set_native():
    s = set()
    for i in range(10000):
        s.add(i)
    for i in range(10000):
        _ = i in s
    for i in range(10000):
        s.discard(i)


# ==========================================
# 5. MAP WORKLOADS
# ==========================================
def bench_map_py():
    m = stl_map(use_rust=False)
    for i in range(10000):
        m.insert(i, i * 2)
    for i in range(10000):
        _ = m.find(i)
    for i in range(10000):
        _ = m.at(i)
    for i in range(10000):
        m.erase(i)


def bench_map_rust():
    m = stl_map(use_rust=True)
    for i in range(10000):
        m.insert(i, i * 2)
    for i in range(10000):
        _ = m.find(i)
    for i in range(10000):
        _ = m.at(i)
    for i in range(10000):
        m.erase(i)


def bench_map_native():
    m = {}
    for i in range(10000):
        m[i] = i * 2
    for i in range(10000):
        _ = i in m
    for i in range(10000):
        _ = m[i]
    for i in range(10000):
        m.pop(i, None)


# ==========================================
# 6. PRIORITY QUEUE WORKLOADS
# ==========================================
def bench_priority_queue_py():
    pq = priority_queue(use_rust=False)
    for i in range(20000):
        pq.push(i)
    for _ in range(20000):
        _ = pq.top()
        pq.pop()


def bench_priority_queue_rust():
    pq = priority_queue(use_rust=True)
    for i in range(20000):
        pq.push(i)
    for _ in range(20000):
        _ = pq.top()
        pq.pop()


def bench_priority_queue_native():
    pq = []
    for i in range(20000):
        heapq.heappush(pq, i)
    for _ in range(20000):
        if pq:
            _ = pq[0]
            heapq.heappop(pq)


# ==========================================
# MAIN EXECUTION
# ==========================================
def main():
    print("=============================================================")
    print("      PythonSTL Comprehensive Container Benchmark Suite      ")
    print("=============================================================\n")
    
    results = {}
    
    # 1. Stack
    py_t, rust_t, nat_t = run_benchmark("Stack (500,000 cycles)", bench_stack_py, bench_stack_rust, STACK_RUST_AVAILABLE, bench_stack_native)
    results["Stack"] = (py_t, rust_t, nat_t, STACK_RUST_AVAILABLE)
    
    # 2. Queue
    py_t, rust_t, nat_t = run_benchmark("Queue (500,000 cycles)", bench_queue_py, bench_queue_rust, QUEUE_RUST_AVAILABLE, bench_queue_native)
    results["Queue"] = (py_t, rust_t, nat_t, QUEUE_RUST_AVAILABLE)
    
    # 3. Vector
    py_t, rust_t, nat_t = run_benchmark("Vector (10,000 push/access + 100 inserts)", bench_vector_py, bench_vector_rust, VECTOR_RUST_AVAILABLE, bench_vector_native)
    results["Vector"] = (py_t, rust_t, nat_t, VECTOR_RUST_AVAILABLE)
    
    # 4. Set
    py_t, rust_t, nat_t = run_benchmark("Set (10,000 inserts/finds/erases)", bench_set_py, bench_set_rust, SET_RUST_AVAILABLE, bench_set_native)
    results["Set"] = (py_t, rust_t, nat_t, SET_RUST_AVAILABLE)
    
    # 5. Map
    py_t, rust_t, nat_t = run_benchmark("Map (10,000 inserts/finds/ats/erases)", bench_map_py, bench_map_rust, MAP_RUST_AVAILABLE, bench_map_native)
    results["Map"] = (py_t, rust_t, nat_t, MAP_RUST_AVAILABLE)
    
    # 6. Priority Queue
    py_t, rust_t, nat_t = run_benchmark("Priority Queue (20,000 push/pops)", bench_priority_queue_py, bench_priority_queue_rust, PQ_RUST_AVAILABLE, bench_priority_queue_native)
    results["Priority Queue"] = (py_t, rust_t, nat_t, PQ_RUST_AVAILABLE)
    
    print("\n" + "=" * 90)
    print("                              PERFORMANCE SUMMARY TABLE                              ")
    print("=" * 90)
    print(f"{'Container Class':<18} | {'Pure Python':<12} | {'Python + Rust':<15} | {'Native Built-in':<17} | {'Rust Speedup vs Py':<18}")
    print("-" * 90)
    
    for container, (py_time, rust_time, native_time, is_rust) in results.items():
        py_str = f"{py_time:.4f}s"
        native_str = f"{native_time:.4f}s"
        if is_rust and rust_time is not None:
            rust_str = f"{rust_time:.4f}s"
            speedup = py_time / rust_time
            status = f"{speedup:.2f}x faster"
        else:
            rust_str = "N/A"
            status = "Pure Py Fallback"
            
        print(f"{container:<18} | {py_str:<12} | {rust_str:<15} | {native_str:<17} | {status:<18}")
        
    print("=========================================================================================")
    print("Note:")
    print("1. 'Pure Python' set/map now run AVL Trees (sorted) vs C++ (BTreeSet/BTreeMap).")
    print("2. 'Native Built-ins' (hash tables) are unsorted and perform at O(1) average case complexity.")
    print("=========================================================================================")


if __name__ == "__main__":
    main()
