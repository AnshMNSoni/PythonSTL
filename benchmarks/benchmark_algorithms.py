import time
import subprocess
import os
import sys
import gc
from pathlib import Path

# Add project root to path to run directly from development folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pythonstl import next_permutation, nth_element, partition, stl_set
from pythonstl.containers.algorithms import RUST_AVAILABLE

def run_py_permutation():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while next_permutation(arr, use_rust=False):
        pass

def run_rust_permutation():
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while next_permutation(arr, use_rust=True):
        pass

def run_py_nth_element():
    arr = list(range(50000, 0, -1))
    nth_element(arr, 25000, use_rust=False)

def run_rust_nth_element():
    arr = list(range(50000, 0, -1))
    nth_element(arr, 25000, use_rust=True)

def run_py_partition():
    arr = list(range(100000))
    partition(arr, lambda x: x % 2 == 0, use_rust=False)

def run_rust_partition():
    arr = list(range(100000))
    partition(arr, lambda x: x % 2 == 0, use_rust=True)

# ----------------- FFI/Execution Framework -----------------

def compile_cpp():
    bench_dir = Path(__file__).parent
    cpp_source = bench_dir / "benchmark_native.cpp"
    cpp_exe = bench_dir / ("benchmark_native.exe" if os.name == 'nt' else "benchmark_native")
    
    try:
        subprocess.run(
            ["g++", "-O3", str(cpp_source), "-o", str(cpp_exe)],
            check=True,
            capture_output=True
        )
        return cpp_exe
    except Exception:
        return None

def run_cpp_benchmark(cpp_exe, arg):
    try:
        result = subprocess.run([str(cpp_exe), arg], check=True, capture_output=True, text=True)
        return float(result.stdout.strip())
    except Exception:
        return None

def run_test(name, py_func, rust_func):
    print(f"Benchmarking {name}...")
    
    gc.collect()
    start = time.perf_counter()
    py_func()
    py_t = time.perf_counter() - start
    
    rust_t = None
    if RUST_AVAILABLE:
        gc.collect()
        start = time.perf_counter()
        rust_func()
        rust_t = time.perf_counter() - start
        
    return py_t, rust_t

def main():
    print("=============================================================")
    print("           PythonSTL Performance Benchmark: Algorithms       ")
    print("=============================================================\n")
    
    cpp_exe = compile_cpp()
    
    # Run tests
    py_perm, rust_perm = run_test("next_permutation (9 elements, 362,880 cycles)", run_py_permutation, run_rust_permutation)
    cpp_perm = run_cpp_benchmark(cpp_exe, "next_permutation") if cpp_exe else None
    
    py_nth, rust_nth = run_test("nth_element (50,000 reversed items, find median)", run_py_nth_element, run_rust_nth_element)
    cpp_nth = run_cpp_benchmark(cpp_exe, "nth_element") if cpp_exe else None
    
    py_part, rust_part = run_test("partition (100,000 items, evens/odds)", run_py_partition, run_rust_partition)
    cpp_part = run_cpp_benchmark(cpp_exe, "partition") if cpp_exe else None
    
    # Cleanup compiled binary
    if cpp_exe and cpp_exe.exists():
        try:
            cpp_exe.unlink()
        except Exception:
            pass
            
    print("\n" + "=" * 70)
    print("                    ALGORITHMS PERFORMANCE TABLE             ")
    print("=" * 70)
    print(f"{'Algorithm Name':<22} | {'Pure Python':<12} | {'Python + Rust':<15} | {'Pure C++ (O3)':<15}")
    print("-" * 70)
    
    def format_row(name, py_t, rust_t, cpp_t):
        py_str = f"{py_t:.4f}s"
        
        if rust_t is not None:
            if rust_t > 0:
                rust_speedup = py_t / rust_t
                rust_str = f"{rust_t:.4f}s ({rust_speedup:.1f}x)"
            else:
                rust_str = f"{rust_t:.4f}s (>1000x)"
        else:
            rust_str = "N/A"
            
        if cpp_t is not None:
            if cpp_t > 0:
                cpp_speedup = py_t / cpp_t
                cpp_str = f"{cpp_t:.4f}s ({cpp_speedup:.1f}x)"
            else:
                cpp_str = f"{cpp_t:.4f}s (>1000x)"
        else:
            cpp_str = "N/A"
            
        print(f"{name:<22} | {py_str:<12} | {rust_str:<15} | {cpp_str:<15}")

    format_row("next_permutation", py_perm, rust_perm, cpp_perm)
    format_row("nth_element", py_nth, rust_nth, cpp_nth)
    format_row("partition", py_part, rust_part, cpp_part)
    print("=============================================================")

if __name__ == "__main__":
    main()
