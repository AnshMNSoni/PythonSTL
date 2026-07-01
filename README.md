# PythonSTL - Python Standard Template Library

[![Downloads](https://static.pepy.tech/badge/pythonstl)](https://pepy.tech/project/pythonstl)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/pythonstl.svg)](https://pypi.org/project/pythonstl/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
<br>

<div align="center">
    <img width="500" height="500" alt="pythonstl_logo" src="https://github.com/user-attachments/assets/7ef83b5f-d005-48e0-a186-05dd7e2221c2" />
</div><br>

A Python package that replicates C++ STL-style data structures using the **Facade Design Pattern**. PythonSTL provides clean, familiar interfaces for developers coming from C++ while maintaining Pythonic best practices.

## Features

- **C++ STL Compliance**: Exact method names and semantics matching C++ STL
- **Facade Design Pattern**: Clean separation between interface and implementation
- **Iterator Support**: STL-style iterators (begin, end, rbegin, rend) and Python iteration
- **Python Integration**: Magic methods (__len__, __bool__, __contains__, __repr__, __eq__)
- **Type Safety**: Full type hints throughout the codebase
- **Copy Operations**: Deep copy support with copy(), __copy__(), and __deepcopy__()
- **Comprehensive Documentation**: Detailed docstrings with time complexity annotations
- **Production Quality**: Proper error handling, PEP8 compliance, and extensive testing
- **Zero Dependencies**: Core package has no external dependencies

## 📦 Installation

```bash
pip install pythonstl
```

Or install from source:

```bash
git clone https://github.com/AnshMNSoni/PythonSTL.git
cd PythonSTL
pip install -e .
```

## Quick Start

```python
from pythonstl import stack, queue, vector, stl_set, stl_map, priority_queue

# Stack (LIFO) - Now with Python magic methods!
s = stack()
s.push(10)
s.push(20)
print(s.top())      # 20
print(len(s))       # 2 - Python len() support
print(bool(s))      # True - Python bool() support

# Vector (Dynamic Array) - With iterators!
v = vector()
v.push_back(100)
v.push_back(200)
v.push_back(300)
v.reserve(1000)     # Pre-allocate capacity
print(len(v))       # 3
print(200 in v)     # True - Python 'in' operator

# Iterate using STL-style iterators
for elem in v.begin():
    print(elem)

# Or use Python iteration
for elem in v:
    print(elem)

# Set (Unique Elements) - With magic methods
s = stl_set()
s.insert(5)
s.insert(10)
print(5 in s)       # True
print(len(s))       # 2

# Map (Key-Value Pairs) - With iteration
m = stl_map()
m.insert("key1", 100)
m.insert("key2", 200)
print("key1" in m)  # True
for key, value in m:
    print(f"{key}: {value}")

# Priority Queue - With comparator support
pq_max = priority_queue(comparator="max")  # Max-heap (default)
pq_min = priority_queue(comparator="min")  # Min-heap
pq_max.push(30)
pq_max.push(10)
pq_max.push(20)
print(pq_max.top())  # 30
```

## Data Structures

### Stack

LIFO (Last-In-First-Out) container adapter.

**Methods:**
- `push(value)` - Add element to top
- `pop()` - Remove top element
- `top()` - Access top element
- `empty()` - Check if empty
- `size()` - Get number of elements
- `copy()` - Create deep copy

**Python Integration:**
- `len(s)` - Get size
- `bool(s)` - Check if non-empty
- `repr(s)` - String representation
- `s1 == s2` - Equality comparison

### Queue

FIFO (First-In-First-Out) container adapter.

**Methods:**
- `push(value)` - Add element to back
- `pop()` - Remove front element
- `front()` - Access front element
- `back()` - Access back element
- `empty()` - Check if empty
- `size()` - Get number of elements
- `copy()` - Create deep copy

**Python Integration:**
- `len(q)` - Get size
- `bool(q)` - Check if non-empty
- `repr(q)` - String representation
- `q1 == q2` - Equality comparison

### Vector

Dynamic array with capacity management.

**Methods:**
- `push_back(value)` - Add element to end
- `pop_back()` - Remove last element
- `at(index)` - Access element with bounds checking
- `insert(position, value)` - Insert element at position
- `erase(position)` - Remove element at position
- `clear()` - Remove all elements
- `reserve(capacity)` - Pre-allocate capacity
- `shrink_to_fit()` - Reduce capacity to size
- `size()` - Get number of elements
- `capacity()` - Get current capacity
- `empty()` - Check if empty
- `begin()` - Get forward iterator
- `end()` - Get end iterator
- `rbegin()` - Get reverse iterator
- `rend()` - Get reverse end iterator
- `copy()` - Create deep copy

**Python Integration:**
- `len(v)` - Get size
- `bool(v)` - Check if non-empty
- `value in v` - Check if value exists
- `repr(v)` - String representation
- `v1 == v2` - Equality comparison
- `v1 < v2` - Lexicographic comparison
- `for elem in v` - Python iteration

### Set

Associative container storing unique elements.

**Methods:**
- `insert(value)` - Add element
- `erase(value)` - Remove element
- `find(value)` - Check if element exists
- `empty()` - Check if empty
- `size()` - Get number of elements
- `begin()` - Get iterator
- `end()` - Get end iterator
- `copy()` - Create deep copy

**Python Integration:**
- `len(s)` - Get size
- `bool(s)` - Check if non-empty
- `value in s` - Check if value exists
- `repr(s)` - String representation
- `s1 == s2` - Equality comparison
- `for elem in s` - Python iteration

### Map

Associative container storing key-value pairs.

**Methods:**
- `insert(key, value)` - Add or update key-value pair
- `erase(key)` - Remove key-value pair
- `find(key)` - Check if key exists
- `at(key)` - Access value by key
- `empty()` - Check if empty
- `size()` - Get number of pairs
- `begin()` - Get iterator
- `end()` - Get end iterator
- `copy()` - Create deep copy

**Python Integration:**
- `len(m)` - Get size
- `bool(m)` - Check if non-empty
- `key in m` - Check if key exists
- `repr(m)` - String representation
- `m1 == m2` - Equality comparison
- `for key, value in m` - Python iteration

### Priority Queue

Container adapter providing priority-based access.

**Methods:**
- `push(value)` - Insert element
- `pop()` - Remove top element
- `top()` - Access top element
- `empty()` - Check if empty
- `size()` - Get number of elements
- `copy()` - Create deep copy

**Comparator Support:**
- `priority_queue(comparator="max")` - Max-heap (default)
- `priority_queue(comparator="min")` - Min-heap

**Python Integration:**
- `len(pq)` - Get size
- `bool(pq)` - Check if non-empty
- `repr(pq)` - String representation
- `pq1 == pq2` - Equality comparison

## Time Complexity Reference

| Container | Operation | Complexity |
|-----------|-----------|------------|
| **Stack** | push() | O(1) amortized |
| | pop() | O(1) |
| | top() | O(1) |
| **Queue** | push() | O(1) |
| | pop() | O(1) |
| | front() / back() | O(1) |
| **Vector** | push_back() | O(1) amortized |
| | pop_back() | O(1) |
| | at() | O(1) |
| | insert() | O(n) |
| | erase() | O(n) |
| | reserve() | O(1) |
| | shrink_to_fit() | O(1) |
| **Set** | insert() | O(1) average |
| | erase() | O(1) average |
| | find() | O(1) average |
| **Map** | insert() | O(1) average |
| | erase() | O(1) average |
| | find() | O(1) average |
| | at() | O(1) average |
| **Priority Queue** | push() | O(log n) |
| | pop() | O(log n) |
| | top() | O(1) |

## 🏗️ Architecture

PythonSTL follows the **Facade Design Pattern** with three layers:

1. **Core Layer** (`pythonstl/core/`)
   - Base classes and type definitions
   - Custom exceptions
   - Iterator classes

2. **Implementation Layer** (`pythonstl/implementations/`)
   - Private implementation classes (prefixed with `_`)
   - Efficient use of Python built-ins
   - Not intended for direct user access

3. **Facade Layer** (`pythonstl/facade/`)
   - Public-facing classes
   - Clean, STL-compliant API
   - Delegates to implementation layer

This architecture ensures:
- **Encapsulation**: Internal implementation is hidden
- **Maintainability**: Easy to modify internals without breaking API
- **Testability**: Each layer can be tested independently

## Thread Safety

**Important:** PythonSTL containers are **NOT thread-safe** by default. If you need to use them in a multi-threaded environment, you must provide your own synchronization (e.g., using `threading.Lock`).

```python
import threading
from pythonstl import stack

s = stack()
lock = threading.Lock()

def thread_safe_push(value):
    with lock:
        s.push(value)
```

## Design Decisions

### Why Facade Pattern?

- **Clean API**: Users interact with simple, well-defined interfaces
- **Flexibility**: Internal implementation can change without affecting users
- **Type Safety**: Facade layer enforces type contracts
- **Error Handling**: Consistent error messages across all containers

### Why STL Naming?

- **Familiarity**: C++ developers can use PythonSTL immediately
- **Consistency**: Predictable method names across containers
- **Documentation**: Extensive C++ STL documentation applies

### Python Integration

Full Python integration while maintaining STL compatibility:
- Magic methods for natural Python usage
- Iterator protocol support
- Copy protocol support
- Maintains backward compatibility

## Performance Benchmarks

PythonSTL includes a compiled Rust backend (built with PyO3 and Maturin) for high-performance operations, alongside pure-Python fallbacks. Below are the actual performance comparison results against pure-Python and native C++ (compiled with `g++ -O3`).

### 1. Containers Performance Benchmarks (3-Way Comparison)

| Container Class | Pure Python (STL) | Python + Rust (STL) | Native Built-in | Rust Speedup | Design / Algorithmic Trade-off |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Stack** | 0.2441s | 0.2178s | 0.0667s | **1.12x faster** | Linear stack operations. Limited by FFI call overhead. |
| **Queue** | 0.2445s | 0.2078s | 0.0520s | **1.18x faster** | FIFO operations. Limited by FFI call overhead. |
| **Vector** | 0.0065s | 0.0038s | 0.0015s | **1.70x faster** | Push_back & random access indices. Limited by FFI. |
| **Set** | 0.1572s | 0.0197s | 0.0014s | **8.00x faster** | AVL Tree (Python) vs. BTree (Rust) vs. Unordered Hash Set (Native). |
| **Map** | 0.1632s | 0.0347s | 0.0020s | **4.70x faster** | AVL Tree (Python) vs. BTree (Rust) vs. Unordered Hash Map (Native). |
| **Priority Queue**| 0.0238s | 0.0371s | 0.0054s | *0.64x faster* | Custom binary heap vs. C-optimized `heapq` module. |

* **Sorted Trees vs. Hash Tables**: Python's native `set` and `dict` are highly optimized $O(1)$ hash tables written in C. PythonSTL sets/maps replicate C++'s `std::set`/`std::map` using sorted trees (`BTreeSet`/`BTreeMap`), which run in $O(\log N)$ and sort keys.
* **FFI overhead**: Storing arbitrary Python objects in Rust requires acquiring the GIL and calling back into the Python VM for comparisons, creating high FFI boundaries.

### 2. Algorithms Suite

| Algorithm Name | Pure Python (Middle Pivot) | Python + Rust | Pure C++ (O3) | Rust Speedup | Design & FFI Insights |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **next_permutation** | 0.2413s | 0.1428s | 0.0000s | **1.7x** | Lexicographical rearrangement. Limited by FFI conversions. |
| **nth_element** | 0.0064s | 0.0052s | 0.0000s | **1.2x** | Quickselect median find. (Previously **70.85s** before optimization). |
| **partition** | 0.0227s | 0.0164s | 0.0003s | **1.4x** | Lambda-predicate partitioning. Dominated by FFI callback overhead. |

* **Algorithmic Pivot Vulnerabilities**: A naive Lomuto partition (`pivot = arr[right]`) causes $O(N^2)$ worst-case time on already-sorted or reversed lists (taking **70.85s**). By switching PythonSTL to a middle-pivot (`arr[mid]`), we restore $O(N)$ average time (**0.0064s**).

### 3. Binary Search (5,000 Queries on 1,000,000 elements)

| Search Mode / Comparator | Pure Python | Python + Rust | Pure C++ (O3) | Rust Speedup | Systems & Design Insights |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Standard (`<` comparison)** | 0.0182s | 0.0034s | 0.0000s | **5.3x** | Preserves $O(\log N)$ via direct list indexing. |
| **Custom Comparator (lambda)**| 0.0180s | 0.0078s | N/A | **2.3x** | Overcomes Python loop overhead despite FFI callbacks. |

* **Direct Indexing**: Instead of extracting/copying the entire list (an $O(N)$ operation), the Rust backend uses direct GIL-bound indexing (`arr.get_item(mid)`), maintaining the strict $O(\log N)$ search complexity.


## ⚠️ Performance Characteristics & Limitations

While PythonSTL provides powerful optimizations, it is essential to understand the systems-level design characteristics and FFI boundaries when using this library:

1. **FFI (Foreign Function Interface) Overhead on Granular Operations:**
   * For container methods like `stack.push()` / `pop()` or `queue.push()` / `pop()`, the Rust backend is only marginally faster (around **1.3x - 1.5x**) than pure Python.
   * **Why:** Calling a compiled function from Python space millions of times introduces constant-factor FFI boundary crossing overhead (argument validation, GIL checks, etc.) that dominates the execution time.
   * **Guidance:** The Rust backend excels at **computation-intensive algorithms** (like `bubble_sort` running **190x+ faster** or `binary_search` running **5x+ faster**) that cross the FFI boundary only once.

2. **Sorted Trees vs. Hash Tables (Set & Map):**
   * Rust-backed `stl_set` and `stl_map` are slower than Python's native `set` and `dict`.
   * **Why:** Python's native sets/dicts are highly optimized unordered hash tables ($O(1)$ average complexity). Replicating C++ STL associative compliance requires sorted trees (Rust's `BTreeSet` and `BTreeMap`), which run in $O(\log N)$ time and execute callbacks into the Python VM for custom comparisons.
   * **Guidance:** Use `stl_set`/`stl_map` when you explicitly require keys to be maintained in **sorted order** (e.g., for range/boundary lookups) matching standard C++ semantics, rather than simple hash-lookup speed.


## Testing

Run the test suite:

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest tests/ --cov=pythonstl --cov-report=html
```

## Development

### Setup

```bash
git clone https://github.com/AnshMNSoni/PythonSTL.git
cd PythonSTL
pip install -e ".[dev]"
```

### Code Quality

```bash
# Type checking
mypy pythonstl/

# Linting
flake8 pythonstl/

# Run all checks
pytest && mypy pythonstl/ && flake8 pythonstl/
```

## ❓ Myths & Common Misconceptions

### Myth 1: "This library has no actual use because online platforms (LeetCode, Codeforces) don't support external libraries."
* **Reality:** Correct! You cannot import external packages during live programming contests. The goal of `PythonSTL` is **not** to be used in live contests. Instead, it serves as a local prototyping, learning, and transition tool. C++ developers moving to Python can use it locally to adapt their mental model of STL data structures to Python's syntax, and to practice structure design during mock interviews.

### Myth 2: "Python's native structures are better and faster, so the Rust backend is unnecessary over-engineering."
* **Reality:** While Python's built-ins are great, Python actually lacks native equivalents for some core STL behaviors:
  - **No Sorted Set/Map:** Python's built-in `set` and `dict` are hash-based and unordered. To maintain a sorted collection, you'd have to sort repeatedly ($\mathcal{O}(n \log n)$). `PythonSTL`'s Rust backend provides a true $\mathcal{O}(\log n)$ sorted `BTreeSet` and `BTreeMap` (and the pure-Python fallback uses a balanced AVL Tree).
  - **No Customizable Priority Queue:** Python’s `heapq` is strictly a min-heap, and custom comparators are difficult to write. `PythonSTL` provides max/min heaps and custom sorting keys out-of-the-box.
  - **Engineering Showcase:** The Rust backend built via Maturin and PyO3 demonstrates a hybrid performance architecture. In real-world projects (like Polars, Pydantic, or cryptography libraries), performance-critical loops are written in compiled languages and bound to Python. This library serves as an educational blueprint for that pattern.

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add tests for new features
4. Ensure all tests pass
5. Submit a pull request

## Thankyou
## Contact

- GitHub: [@AnshMNSoni](https://github.com/AnshMNSoni)
- Issues: [GitHub Issues](https://github.com/AnshMNSoni/PythonSTL/issues)
- Linkedin: [@anshmnsoni](https://linkedin.com/in/anshmnsoni)

**PythonSTL v1.1.7** - Bringing C++ STL elegance to Python