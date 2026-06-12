import time
import subprocess
import os
import sys
import gc
from pathlib import Path

# Add project root to path to run directly from development folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pythonstl import lower_bound
from pythonstl.facade.algorithms import RUST_AVAILABLE

def run_py_binary_search(arr, targets):
    sum_indices = 0
    for target in targets:
        sum_indices += lower_bound(arr, target, use_rust=False)
    return sum_indices

def run_rust_binary_search(arr, targets):
    sum_indices = 0
    for target in targets:
        sum_indices += lower_bound(arr, target, use_rust=True)
    return sum_indices

def run_py_comp_binary_search(arr, targets, comp):
    sum_indices = 0
    for target in targets:
        sum_indices += lower_bound(arr, target, comp=comp, use_rust=False)
    return sum_indices

def run_rust_comp_binary_search(arr, targets, comp):
    sum_indices = 0
    for target in targets:
        sum_indices += lower_bound(arr, target, comp=comp, use_rust=True)
    return sum_indices

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

def main():
    print("=============================================================")
    print("        PythonSTL Performance Benchmark: Binary Search       ")
    print("=============================================================\n")
    
    # 1. Setup sorted array of 1,000,000 elements
    print("Generating 1,000,000 elements sorted array...")
    arr = [i * 2 for i in range(1000000)]
    targets = [q * 3 for q in range(5000)]
    
    cpp_exe = compile_cpp()
    
    # Standard comparisons (Pure Py vs Rust vs C++)
    print("Running standard binary search (5,000 queries)...")
    gc.collect()
    start = time.perf_counter()
    run_py_binary_search(arr, targets)
    py_t = time.perf_counter() - start
    
    rust_t = None
    if RUST_AVAILABLE:
        gc.collect()
        start = time.perf_counter()
        run_rust_binary_search(arr, targets)
        rust_t = time.perf_counter() - start
        
    cpp_t = run_cpp_benchmark(cpp_exe, "binary_search") if cpp_exe else None
    
    # Custom comparator comparisons (how slow is FFI callback?)
    print("Running custom comparator binary search (5,000 queries)...")
    comp = lambda a, b: a < b
    
    gc.collect()
    start = time.perf_counter()
    run_py_comp_binary_search(arr, targets, comp)
    py_comp_t = time.perf_counter() - start
    
    rust_comp_t = None
    if RUST_AVAILABLE:
        gc.collect()
        start = time.perf_counter()
        run_rust_comp_binary_search(arr, targets, comp)
        rust_comp_t = time.perf_counter() - start
        
    # Cleanup compiled binary
    if cpp_exe and cpp_exe.exists():
        try:
            cpp_exe.unlink()
        except Exception:
            pass
            
    print("\n" + "=" * 70)
    print("                 BINARY SEARCH PERFORMANCE TABLE             ")
    print("=" * 70)
    print(f"{'Search Mode / Comparator':<26} | {'Pure Python':<12} | {'Python + Rust':<15} | {'Pure C++ (O3)':<15}")
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
            
        print(f"{name:<26} | {py_str:<12} | {rust_str:<15} | {cpp_str:<15}")

    format_row("Standard (< comparison)", py_t, rust_t, cpp_t)
    format_row("Custom Comparator (lambda)", py_comp_t, rust_comp_t, None)
    print("=============================================================")

if __name__ == "__main__":
    main()
