# PythonSTL - Python Standard Template Library

[![Downloads](https://static.pepy.tech/badge/pythonstl)](https://pepy.tech/project/pythonstl)
[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/pythonstl.svg)](https://pypi.org/project/pythonstl/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
<br>

<div align="center">
    <img width="500" height="500" alt="pythonstl-removebg-preview" src="https://github.com/user-attachments/assets/83bc0da7-50d5-489b-a19d-c8e04fe73cca" />
</div><br>

A Python package that replicates C++ STL-style data structures using a modular **Containers**, **Engines**, and **Utility** architecture. PythonSTL provides clean, familiar interfaces for developers coming from C++ while maintaining Pythonic best practices.

## Features

- **C++ STL Compliance**: Exact method names and semantics matching C++ STL
- **Modular Layered Architecture**: Clean separation between containers, execution engines, and utilities
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

PythonSTL is structured into three distinct, specialized layers (**Containers**, **Engines**, **Utility**):

1. **Containers Layer** (`pythonstl/containers/`)
   - Public-facing STL-compliant container classes and algorithms
   - Dispatches operations to native Rust or Python engines
   - Clean, C++ STL-compliant API

2. **Engines Layer** (`pythonstl/engines/`)
   - Internal execution and storage engine implementations (prefixed with `_`)
   - Linear, associative, and heap structure engines
   - Not intended for direct user access

3. **Utility Layer** (`pythonstl/utility/`)
   - Common utilities, base classes, and type definitions
   - Custom exception types
   - Iterator implementations and AVL tree building blocks

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

### Why Containers, Engines & Utility?

- **Clean API**: Users interact with simple, well-defined container interfaces
- **Flexibility**: Internal storage and execution engines can change without affecting users
- **Type Safety**: Containers layer enforces type contracts
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

PythonSTL includes a compiled Rust backend (built with PyO3 and Maturin) for high-performance operations, alongside pure-Python fallbacks. 

### ⚠️ A Note on Algorithmic and FFI Characteristics

When comparing PySTL to Python's built-ins, it is crucial to recognize two key system characteristics:
1. **Sorted Tree-based vs. Hash-based Complexity:** Python's native `dict` and `set` are unordered hash tables with average **$O(1)$** lookup/insert complexity. PySTL's `stl_map` and `set` are modeled after C++'s `std::map`/`std::set` (using `BTreeMap`/`BTreeSet` in Rust and an `AVLTree` in Python) which maintain keys in **sorted order**, yielding **$O(\log N)$** lookup/insert complexity. Direct speed comparison between them is algorithmically an "apples-to-oranges" comparison.
2. **FFI Boundary Crossing Overhead:** For high-frequency, low-work operations (like pushing single elements), the cost of crossing the Python-Rust FFI boundary is the dominant overhead factor.

To isolate the actual performance gains of using the Rust backend, PySTL benchmarks compare the **Rust-backed STL containers** against their **Pure Python STL container counterparts** (equivalent data structures and APIs), alongside Python's built-ins as a baseline.

### 1. Containers Performance (10,000 Elements / Operations)

| Container Class & Operation | Pure Python STL | Python + Rust STL | Native Built-in | Rust Speedup (vs Pure Py STL) |
| :--- | :--- | :--- | :--- | :--- |
| **Stack (1,000,000 push/pops)** | 0.4768s | 0.3227s | 0.0530s (Native list.pop) | **1.48x faster** |
| **Vector (10,000 push_backs)** | 0.2296s | 0.1374s | 0.0444s (Native list.append) | **1.67x faster** |
| **Vector (10,000 random at())** | 0.4844s | 0.3264s | 0.0586s (Native list[i]) | **1.48x faster** |
| **Map (10,000 insert - integers)** | 0.0873s | 0.0116s | 0.0019s (Native dict[key]) | **7.53x faster** |
| **Map (10,000 find - integers)**   | 0.0077s | 0.0046s | 0.0018s (Native key in dict) | **1.68x faster** |

*Note: For primitive key types (like integers, floats, and strings), the Rust BTreeMap/BTreeSet uses native type-extraction fast-paths in `PyObjectOrd::cmp` to avoid calling back into CPython's rich comparison system.*

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
  - **No Sorted Set/Map:** Python's built-in `set` and `dict` are hash-based and unordered. To maintain a sorted collection, you'd have to sort repeatedly $\mathcal{O}(n \log n)$. `PythonSTL`'s Rust backend provides a true $\mathcal{O}(\log n)$ sorted `BTreeSet` and `BTreeMap` (and the pure-Python fallback uses a balanced AVL Tree).
  - **No Customizable Priority Queue:** Python’s `heapq` is strictly a min-heap, and custom comparators are difficult to write. `PythonSTL` provides max/min heaps and custom sorting keys out-of-the-box.
  - **Engineering Showcase:** The Rust backend built via Maturin and PyO3 demonstrates a hybrid performance architecture. In real-world projects (like Polars, Pydantic, or cryptography libraries), performance-critical loops are written in compiled languages and bound to Python. This library serves as an educational blueprint for that pattern.

### Myth 3: "Since there is a Rust backend, every operation must be faster than pure Python."
* **Reality:** Incorrect. As detailed in the performance benchmarks, granular $O(1)$ operations like single element pushes/pops on `stack` or `queue` are dominated by FFI (Foreign Function Interface) boundary crossing overhead. The Rust backend excels in **computation-intensive algorithms** (like sorting, partitioning, or binary searching large arrays) where the FFI boundary is crossed only once or twice, and when type-extraction fast-paths can stay natively in Rust.

### Myth 4: "PySTL's Rust backend makes the containers thread-safe."
* **Reality:** Absolutely not. Even with the Rust backend, PySTL containers are **not thread-safe**. Since they store Python objects (`PyObject`), Rust has to interact with the Python GIL (Global Interpreter Lock). Simultaneous mutations from multiple Python threads on the same container will lead to data races or undefined behavior unless synchronized using Python's `threading.Lock`.

### Myth 5: "PySTL's `stl_set` and `stl_map` are drop-in performance replacements for Python `set` and `dict`."
* **Reality:** No. They serve fundamentally different algorithmic needs. Python `set`/`dict` are hash tables ($O(1)$ average complexity, unordered). PySTL's set/map are tree-based sorted containers ($O(\log N)$ complexity, ordered). They should only be used when keys must be kept sorted or when range query capabilities (like `lower_bound`/`upper_bound`) are needed.

### Myth 6: "Using a Rust backend avoids all Python memory and reference counting issues."
* **Reality:** False. Because PySTL containers store arbitrary Python objects, they hold `PyObject` references. They participate in CPython's reference counting and garbage collection. If you create circular references, CPython's GC still has to clean them up.

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

**PythonSTL v1.1.10** - Bringing C++ STL elegance to Python
