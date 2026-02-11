"""
PySTL v2 Example Usage

This script demonstrates all features of PySTL v2 including:
- STL-style operations
- Python magic methods
- Iterator support
- Copy operations
- New vector methods
- Priority queue comparators
"""

from pythonstl import stack, queue, vector, stl_set, stl_map, priority_queue
from pythonstl import EmptyContainerError, OutOfRangeError, KeyNotFoundError
from copy import copy, deepcopy


def demonstrate_stack():
    """Demonstrate stack operations with v2 features."""
    print("=" * 60)
    print("STACK DEMONSTRATION")
    print("=" * 60)
    
    s = stack()
    s.push(10)
    s.push(20)
    s.push(30)
    
    print(f"Stack after pushes: {s}")
    print(f"Top element: {s.top()}")
    print(f"Size (using len()): {len(s)}")
    print(f"Is non-empty (using bool()): {bool(s)}")
    
    # Copy operations
    s_copy = s.copy()
    s_deepcopy = deepcopy(s)
    print(f"Original == Copy: {s == s_copy}")
    
    s.pop()
    print(f"After pop: {s}")
    print()


def demonstrate_queue():
    """Demonstrate queue operations with v2 features."""
    print("=" * 60)
    print("QUEUE DEMONSTRATION")
    print("=" * 60)
    
    q = queue()
    q.push(1)
    q.push(2)
    q.push(3)
    
    print(f"Queue after pushes: {q}")
    print(f"Front element: {q.front()}")
    print(f"Back element: {q.back()}")
    print(f"Size (using len()): {len(q)}")
    
    # Copy operations
    q_copy = copy(q)
    print(f"Original == Copy: {q == q_copy}")
    
    q.pop()
    print(f"After pop: {q}")
    print()


def demonstrate_vector():
    """Demonstrate vector operations with v2 features."""
    print("=" * 60)
    print("VECTOR DEMONSTRATION")
    print("=" * 60)
    
    v = vector()
    v.push_back(100)
    v.push_back(200)
    v.push_back(300)
    v.push_back(400)
    
    print(f"Vector: {v}")
    print(f"Size: {len(v)}")
    print(f"Capacity: {v.capacity()}")
    
    # New v2 methods
    v.reserve(1000)
    print(f"After reserve(1000), capacity: {v.capacity()}")
    
    v.shrink_to_fit()
    print(f"After shrink_to_fit(), capacity: {v.capacity()}")
    
    # Python integration
    print(f"200 in vector: {200 in v}")
    print(f"500 in vector: {500 in v}")
    
    # Iterator support
    print("\nForward iteration:")
    for elem in v:
        print(f"  {elem}")
    
    print("\nReverse iteration:")
    for elem in v.rbegin():
        print(f"  {elem}")
    
    # Comparison
    v2 = vector()
    v2.push_back(100)
    v2.push_back(200)
    v2.push_back(300)
    v2.push_back(400)
    print(f"\nv == v2: {v == v2}")
    print(f"v < v2: {v < v2}")
    
    # Copy operations
    v_copy = v.copy()
    print(f"Copy successful: {v == v_copy}")
    print()


def demonstrate_set():
    """Demonstrate set operations with v2 features."""
    print("=" * 60)
    print("SET DEMONSTRATION")
    print("=" * 60)
    
    s = stl_set()
    s.insert(5)
    s.insert(10)
    s.insert(15)
    s.insert(10)  # Duplicate, won't be added
    
    print(f"Set: {s}")
    print(f"Size: {len(s)}")
    
    # Python integration
    print(f"10 in set: {10 in s}")
    print(f"20 in set: {20 in s}")
    
    # Iteration
    print("\nIterating over set:")
    for elem in s:
        print(f"  {elem}")
    
    # STL-style iteration
    print("\nSTL-style iteration:")
    it = s.begin()
    for elem in it:
        print(f"  {elem}")
    
    # Copy operations
    s_copy = deepcopy(s)
    print(f"\nCopy successful: {s == s_copy}")
    
    s.erase(10)
    print(f"After erase(10): {s}")
    print()


def demonstrate_map():
    """Demonstrate map operations with v2 features."""
    print("=" * 60)
    print("MAP DEMONSTRATION")
    print("=" * 60)
    
    m = stl_map()
    m.insert("apple", 100)
    m.insert("banana", 200)
    m.insert("cherry", 300)
    
    print(f"Map: {m}")
    print(f"Size: {len(m)}")
    
    # Python integration
    print(f"'apple' in map: {'apple' in m}")
    print(f"'orange' in map: {'orange' in m}")
    
    # Access
    print(f"Value for 'banana': {m.at('banana')}")
    
    # Iteration
    print("\nIterating over map:")
    for key, value in m:
        print(f"  {key}: {value}")
    
    # Copy operations
    m_copy = m.copy()
    print(f"\nCopy successful: {m == m_copy}")
    
    m.erase("banana")
    print(f"After erase('banana'): {m}")
    print()


def demonstrate_priority_queue():
    """Demonstrate priority queue operations with v2 features."""
    print("=" * 60)
    print("PRIORITY QUEUE DEMONSTRATION")
    print("=" * 60)
    
    # Max-heap (default)
    pq_max = priority_queue(comparator="max")
    pq_max.push(30)
    pq_max.push(10)
    pq_max.push(50)
    pq_max.push(20)
    
    print("Max-Heap Priority Queue:")
    print(f"  {pq_max}")
    print(f"  Top element: {pq_max.top()}")
    print(f"  Size: {len(pq_max)}")
    
    # Min-heap
    pq_min = priority_queue(comparator="min")
    pq_min.push(30)
    pq_min.push(10)
    pq_min.push(50)
    pq_min.push(20)
    
    print("\nMin-Heap Priority Queue:")
    print(f"  {pq_min}")
    print(f"  Top element: {pq_min.top()}")
    print(f"  Size: {len(pq_min)}")
    
    # Copy operations
    pq_copy = pq_max.copy()
    print(f"\nCopy successful: {pq_max == pq_copy}")
    
    print("\nExtracting from max-heap:")
    while not pq_max.empty():
        print(f"  {pq_max.top()}")
        pq_max.pop()
    print()


def demonstrate_error_handling():
    """Demonstrate error handling."""
    print("=" * 60)
    print("ERROR HANDLING DEMONSTRATION")
    print("=" * 60)
    
    # Empty container error
    try:
        s = stack()
        s.top()  # Error: empty stack
    except EmptyContainerError as e:
        print(f"EmptyContainerError: {e}")
    
    # Out of range error
    try:
        v = vector()
        v.push_back(10)
        v.at(5)  # Error: index out of range
    except OutOfRangeError as e:
        print(f"OutOfRangeError: {e}")
    
    # Key not found error
    try:
        m = stl_map()
        m.insert("key1", 100)
        m.at("key2")  # Error: key not found
    except KeyNotFoundError as e:
        print(f"KeyNotFoundError: {e}")
    
    print()


def demonstrate_copy_semantics():
    """Demonstrate deep copy vs shallow copy."""
    print("=" * 60)
    print("COPY SEMANTICS DEMONSTRATION")
    print("=" * 60)
    
    # Create a vector with mutable objects
    v1 = vector()
    v1.push_back([1, 2, 3])
    v1.push_back([4, 5, 6])
    
    # Shallow copy (copy.copy)
    v2 = copy(v1)
    
    # Deep copy (copy.deepcopy)
    v3 = deepcopy(v1)
    
    print(f"Original: {v1}")
    print(f"Shallow copy: {v2}")
    print(f"Deep copy: {v3}")
    
    # All are equal
    print(f"\nv1 == v2: {v1 == v2}")
    print(f"v1 == v3: {v1 == v3}")
    
    print("\nNote: All PySTL copy operations are deep copies by default")
    print("to ensure data independence.")
    print()


def main():
    """Run all demonstrations."""
    print("\n")
    print("╔" + "=" * 58 + "╗")
    print("║" + " " * 12 + "PySTL v2 - Feature Demonstration" + " " * 13 + "║")
    print("╚" + "=" * 58 + "╝")
    print()
    
    demonstrate_stack()
    demonstrate_queue()
    demonstrate_vector()
    demonstrate_set()
    demonstrate_map()
    demonstrate_priority_queue()
    demonstrate_error_handling()
    demonstrate_copy_semantics()
    
    print("=" * 60)
    print("All demonstrations completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()
