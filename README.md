# PythonSTL - Python Standard Template Library

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://img.shields.io/pypi/v/pythonstl.svg)](https://pypi.org/project/pythonstl/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.1-brightgreen.svg)](https://github.com/AnshMNSoni/PythonSTL)

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

## Benchmarks

PythonSTL provides benchmarks comparing performance against Python built-ins:

```bash
python benchmarks/benchmark_stack.py
python benchmarks/benchmark_vector.py
python benchmarks/benchmark_map.py
```

**Expected Overhead:** 1.1x - 1.5x compared to native Python structures

The facade pattern adds minimal overhead while providing:
- STL-style API
- Better error messages
- Bounds checking
- Type safety

See `benchmarks/README.md` for detailed analysis.

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

## 🛠️ Development

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

## Note
➡️ The goal is NOT to replace Python built-ins.<br>
➡️ The goal is to provide: 1) Conceptual clarity 2) STL familiarity for C++ developers 3) A structured learning bridge for DSA <br>

## 📝 License

MIT License - see LICENSE file for details.

## 🤝 Contributing

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

**PythonSTL v0.1.0** - Bringing C++ STL elegance to Python
