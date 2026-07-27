import time
import subprocess
import os
import sys
from pathlib import Path

# Add project root to path to run directly from development folder
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pythonstl.containers.stack import stack, RUST_AVAILABLE

# Try importing the bubble_sort function from the compiled Rust library
try:
    from pythonstl._rust import bubble_sort as rust_bubble_sort
    HAS_RUST_SORT = True
except ImportError:
    HAS_RUST_SORT = False

def run_python_stack_benchmark():
    print("Running Pure Python Stack benchmark...")
    s = stack(use_rust=False)
    
    start = time.perf_counter()
    for i in range(1000000):
        s.push(i)
    for _ in range(1000000):
        s.pop()
    end = time.perf_counter()
    
    return end - start

def run_rust_stack_benchmark():
    if not RUST_AVAILABLE:
        print("Python + Rust Stack is not available (Rust binary not compiled). Skipping...")
        return None
        
    print("Running Python + Rust Stack benchmark...")
    s = stack(use_rust=True)
    
    start = time.perf_counter()
    for i in range(1000000):
        s.push(i)
    for _ in range(1000000):
        s.pop()
    end = time.perf_counter()
    
    return end - start

# ----------------- Sorting Benchmarks -----------------

def python_bubble_sort(arr):
    arr = list(arr)
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def run_python_sort_benchmark(arr):
    print("Running Pure Python Bubble Sort (10,000 items)...")
    start = time.perf_counter()
    python_bubble_sort(arr)
    end = time.perf_counter()
    return end - start

def run_rust_sort_benchmark(arr):
    if not HAS_RUST_SORT:
        print("Rust bubble_sort is not compiled. Skipping...")
        return None
    print("Running Python + Rust Bubble Sort (10,000 items)...")
    start = time.perf_counter()
    rust_bubble_sort(list(arr))
    end = time.perf_counter()
    return end - start

# ----------------- Native C++ Executions -----------------

def compile_cpp():
    bench_dir = Path(__file__).parent
    cpp_source = bench_dir / "benchmark_native.cpp"
    cpp_exe = bench_dir / ("benchmark_native.exe" if os.name == 'nt' else "benchmark_native")
    
    print("Checking C++ compiler...")
    try:
        # Compile the C++ program with optimizations enabled (-O3)
        print("Compiling native C++ benchmark (g++ -O3)...")
        subprocess.run(
            ["g++", "-O3", str(cpp_source), "-o", str(cpp_exe)],
            check=True,
            capture_output=True
        )
        return cpp_exe
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"Failed to compile C++ benchmark: {e}. Skipping C++ baseline.")
        return None

def run_cpp_benchmark(cpp_exe, arg):
    print(f"Running compiled C++ benchmark ({arg})...")
    try:
        result = subprocess.run([str(cpp_exe), arg], check=True, capture_output=True, text=True)
        cpp_time = float(result.stdout.strip())
        return cpp_time
    except Exception as e:
        print(f"Failed to run C++ benchmark ({arg}): {e}")
        return None

def main():
    print("============================================================")
    print("           PythonSTL Performance Benchmark Suit             ")
    print("============================================================")
    
    # Compilation
    cpp_exe = compile_cpp()
    print()

    # --- BENCHMARK 1: Stack ---
    print("------------------------------------------------------------")
    print(" BENCHMARK 1: Stack (1,000,000 push/pop cycles)")
    print(" Note: High number of Python-Rust boundary crossings")
    print("------------------------------------------------------------")
    
    py_stack = run_python_stack_benchmark()
    print(f"Pure Python Stack: {py_stack:.4f} seconds")
    
    rust_stack = run_rust_stack_benchmark()
    if rust_stack is not None:
        print(f"Python + Rust Stack: {rust_stack:.4f} seconds")
        
    cpp_stack = None
    if cpp_exe is not None:
        cpp_stack = run_cpp_benchmark(cpp_exe, "stack")
        if cpp_stack is not None:
            print(f"Pure C++ Stack: {cpp_stack:.4f} seconds")
    print()

    # --- BENCHMARK 2: Bubble Sort ---
    print("------------------------------------------------------------")
    print(" BENCHMARK 2: Bubble Sort (10,000 reversed items)")
    print(" Note: Single boundary crossing, heavy computational load")
    print("------------------------------------------------------------")
    
    sort_data = list(range(10000, 0, -1))
    
    py_sort = run_python_sort_benchmark(sort_data)
    print(f"Pure Python Sort: {py_sort:.4f} seconds")
    
    rust_sort_time = run_rust_sort_benchmark(sort_data)
    if rust_sort_time is not None:
        print(f"Python + Rust Sort: {rust_sort_time:.4f} seconds")
        
    cpp_sort = None
    if cpp_exe is not None:
        cpp_sort = run_cpp_benchmark(cpp_exe, "sort")
        if cpp_sort is not None:
            print(f"Pure C++ Sort: {cpp_sort:.4f} seconds")
            
    # Cleanup compiled C++ binary
    if cpp_exe is not None and cpp_exe.exists():
        try:
            cpp_exe.unlink()
        except Exception:
            pass
            
    print("\n" + "=" * 60)
    print("                  SUMMARY TABLES & METRICS                  ")
    print("=" * 60)
    
    print("\nTABLE 1: STACK OPERATIONS (1,000,000 Cycles)")
    print(f"{'Implementation':<20} | {'Time (Seconds)':<15} | {'Speedup vs. Python':<20}")
    print("-" * 62)
    print(f"{'Pure Python':<20} | {py_stack:.4f}s{''*8} | {'1.0x (Baseline)':<20}")
    if rust_stack is not None:
        rust_speedup = py_stack / rust_stack
        print(f"{'Python + Rust':<20} | {rust_stack:.4f}s{''*8} | {f'{rust_speedup:.2f}x faster':<20}")
    if cpp_stack is not None:
        cpp_speedup = py_stack / cpp_stack
        print(f"{'Pure C++ (O3)':<20} | {cpp_stack:.4f}s{''*8} | {f'{cpp_speedup:.2f}x faster':<20}")
        
    print("\nTABLE 2: BUBBLE SORT ALGORITHM (10,000 Elements)")
    print(f"{'Implementation':<20} | {'Time (Seconds)':<15} | {'Speedup vs. Python':<20}")
    print("-" * 62)
    print(f"{'Pure Python':<20} | {py_sort:.4f}s{''*8} | {'1.0x (Baseline)':<20}")
    if rust_sort_time is not None:
        rust_speedup = py_sort / rust_sort_time
        print(f"{'Python + Rust':<20} | {rust_sort_time:.4f}s{''*8} | {f'{rust_speedup:.2f}x faster (Maturin)':<20}")
    if cpp_sort is not None:
        cpp_speedup = py_sort / cpp_sort
        print(f"{'Pure C++ (O3)':<20} | {cpp_sort:.4f}s{''*8} | {f'{cpp_speedup:.2f}x faster':<20}")
    print("=" * 60)

if __name__ == "__main__":
    main()
