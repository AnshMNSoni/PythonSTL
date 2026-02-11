# PySTL Benchmarks

This directory contains performance benchmarks comparing PySTL containers against Python's built-in data structures.

## Running Benchmarks

To run all benchmarks:

```bash
python benchmarks/benchmark_stack.py
python benchmarks/benchmark_vector.py
python benchmarks/benchmark_map.py
```

Or run them all at once:

```bash
for file in benchmarks/benchmark_*.py; do python "$file"; echo; done
```

## Benchmark Files

- **benchmark_stack.py**: Compares `pystl.stack` vs Python `list`
- **benchmark_vector.py**: Compares `pystl.vector` vs Python `list`
- **benchmark_map.py**: Compares `pystl.stl_map` vs Python `dict`

## Understanding Results

### Performance Expectations

PySTL containers wrap Python's built-in data structures with a facade pattern, providing:
- **STL-style API**: Familiar interface for C++ developers
- **Type safety**: Better error messages and bounds checking
- **Encapsulation**: Clean separation of interface and implementation

### Overhead Analysis

The facade pattern introduces a small constant-factor overhead:
- **Typical overhead**: 1.1x - 1.5x compared to native Python structures
- **Why**: Additional function call layer and bounds checking
- **Trade-off**: Slightly slower but safer and more maintainable

### When to Use PySTL

Use PySTL when:
- ✅ You want STL-style semantics in Python
- ✅ Code clarity and maintainability are priorities
- ✅ You're migrating from C++ to Python
- ✅ You need consistent error handling

Use native Python structures when:
- ✅ Maximum performance is critical
- ✅ You're comfortable with Python idioms
- ✅ The overhead matters for your use case

## Benchmark Methodology

All benchmarks use Python's `timeit` module with:
- **Iterations**: 100 runs per test
- **Data size**: 10,000 elements (typical workload)
- **Operations tested**: Insert, access, delete, search

## Sample Results

Typical performance ratios (PySTL/Python):
- Stack push/pop: ~1.2x
- Vector push_back: ~1.2x
- Vector at(): ~1.3x (includes bounds checking)
- Map insert: ~1.3x
- Map find: ~1.2x

*Note: Actual results vary by system and Python version.*

## Contributing

To add new benchmarks:
1. Create `benchmark_<container>.py`
2. Follow the existing structure
3. Include comparison with Python built-ins
4. Document the operations being tested
