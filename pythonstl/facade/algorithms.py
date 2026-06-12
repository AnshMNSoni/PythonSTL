"""
C++ STL Algorithms Suite.

This module provides replicas of standard C++ algorithms from <algorithm>
with dynamic Rust backend loading and in-place list mutation.
"""

from typing import Callable, Any

try:
    from pythonstl._rust import next_permutation as _rust_next_permutation
    from pythonstl._rust import prev_permutation as _rust_prev_permutation
    from pythonstl._rust import nth_element as _rust_nth_element
    from pythonstl._rust import partition as _rust_partition
    from pythonstl._rust import lower_bound as _rust_lower_bound
    from pythonstl._rust import upper_bound as _rust_upper_bound
    from pythonstl._rust import binary_search as _rust_binary_search
    from pythonstl._rust import equal_range as _rust_equal_range
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False


# ----------------- Pure-Python Fallbacks -----------------

def _py_next_permutation(arr: list) -> bool:
    n = len(arr)
    if n <= 1:
        return False

    i = n - 2
    while i >= 0 and arr[i] >= arr[i + 1]:
        i -= 1

    if i < 0:
        arr.reverse()
        return False

    j = n - 1
    while arr[j] <= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True


def _py_prev_permutation(arr: list) -> bool:
    n = len(arr)
    if n <= 1:
        return False

    i = n - 2
    while i >= 0 and arr[i] <= arr[i + 1]:
        i -= 1

    if i < 0:
        arr.reverse()
        return False

    j = n - 1
    while arr[j] >= arr[i]:
        j -= 1

    arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])
    return True


def _py_nth_element(arr: list, nth: int) -> None:
    n = len(arr)
    if nth < 0 or nth >= n:
        return

    left = 0
    right = n - 1
    while left < right:
        mid = left + (right - left) // 2
        arr[mid], arr[right] = arr[right], arr[mid]
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]

        pivot_idx = i
        if pivot_idx == nth:
            return
        elif pivot_idx > nth:
            right = pivot_idx - 1
        else:
            left = pivot_idx + 1


def _py_partition(arr: list, predicate: Callable[[Any], bool]) -> int:
    i = 0
    for j in range(len(arr)):
        if predicate(arr[j]):
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    return i


def _py_lower_bound(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None) -> int:
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        mid_val = arr[mid]
        is_less = comp(mid_val, val) if comp else (mid_val < val)
        if is_less:
            left = mid + 1
        else:
            right = mid
    return left


def _py_upper_bound(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None) -> int:
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        mid_val = arr[mid]
        is_less = comp(val, mid_val) if comp else (val < mid_val)
        if is_less:
            right = mid
        else:
            left = mid + 1
    return left


def _py_binary_search(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None) -> bool:
    if not arr:
        return False
    idx = _py_lower_bound(arr, val, comp)
    if idx < len(arr):
        elem = arr[idx]
        if comp:
            return not comp(elem, val) and not comp(val, elem)
        return elem == val
    return False


def _py_equal_range(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None) -> tuple[int, int]:
    return _py_lower_bound(arr, val, comp), _py_upper_bound(arr, val, comp)


# ----------------- Public API Interfaces -----------------

def next_permutation(arr: list, use_rust: bool = True) -> bool:
    """
    Rearranges elements in-place to the next lexicographically greater permutation.

    If the next permutation exists, rearranges elements and returns True.
    Otherwise, reverses the array to the smallest ascending order and returns False.

    Args:
        arr: The list to modify in-place.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Returns:
        True if next permutation exists, False otherwise.

    Time Complexity:
        O(n) where n is len(arr)
    """
    if use_rust and RUST_AVAILABLE:
        return _rust_next_permutation(arr)
    return _py_next_permutation(arr)


def prev_permutation(arr: list, use_rust: bool = True) -> bool:
    """
    Rearranges elements in-place to the next lexicographically smaller permutation.

    If the previous permutation exists, rearranges elements and returns True.
    Otherwise, reverses the array to the largest descending order and returns False.

    Args:
        arr: The list to modify in-place.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Returns:
        True if prev permutation exists, False otherwise.

    Time Complexity:
        O(n) where n is len(arr)
    """
    if use_rust and RUST_AVAILABLE:
        return _rust_prev_permutation(arr)
    return _py_prev_permutation(arr)


def nth_element(arr: list, nth: int, use_rust: bool = True) -> None:
    """
    Partitions the list in-place so that the element at index `nth` is the one
    that would be there if the list were completely sorted.

    All elements preceding `nth` are partitioned to be less than or equal to `nth`.
    All elements succeeding `nth` are partitioned to be greater than or equal to `nth`.
    Does not guarantee sorted order of the surrounding elements.

    Args:
        arr: The list to modify in-place.
        nth: The index that should contain the sorted element.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Time Complexity:
        O(n) average case
    """
    if use_rust and RUST_AVAILABLE:
        _rust_nth_element(arr, nth)
    else:
        _py_nth_element(arr, nth)


def partition(arr: list, predicate: Callable[[Any], bool], use_rust: bool = True) -> int:
    """
    Reorders the elements in the list in-place such that all elements for which
    `predicate` returns True precede all elements for which it returns False.

    Does not guarantee stable relative ordering.

    Args:
        arr: The list to modify in-place.
        predicate: A callable returning True or False for each element.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Returns:
        The boundary index pointing to the first element that returned False.

    Time Complexity:
        O(n) where n is len(arr)
    """
    if use_rust and RUST_AVAILABLE:
        return _rust_partition(arr, predicate)
    return _py_partition(arr, predicate)


def lower_bound(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None, use_rust: bool = True) -> int:
    """
    Returns the index of the first element in the range that does not compare less than `val`.

    Args:
        arr: The sorted list to search.
        val: The value to search for.
        comp: Optional custom binary comparator Callable(a, b) defining custom less-than.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Returns:
        The index of the first element that is >= val, or len(arr) if not found.

    Time Complexity:
        O(log n)
    """
    if use_rust and RUST_AVAILABLE:
        return _rust_lower_bound(arr, val, comp)
    return _py_lower_bound(arr, val, comp)


def upper_bound(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None, use_rust: bool = True) -> int:
    """
    Returns the index of the first element in the range that compares greater than `val`.

    Args:
        arr: The sorted list to search.
        val: The value to search for.
        comp: Optional custom binary comparator Callable(a, b) defining custom less-than.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Returns:
        The index of the first element that is > val, or len(arr) if not found.

    Time Complexity:
        O(log n)
    """
    if use_rust and RUST_AVAILABLE:
        return _rust_upper_bound(arr, val, comp)
    return _py_upper_bound(arr, val, comp)


def binary_search(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None, use_rust: bool = True) -> bool:
    """
    Checks if a value is present in the sorted range.

    Args:
        arr: The sorted list to search.
        val: The value to search for.
        comp: Optional custom binary comparator Callable(a, b) defining custom less-than.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Returns:
        True if the element equivalent to val is found, False otherwise.

    Time Complexity:
        O(log n)
    """
    if use_rust and RUST_AVAILABLE:
        return _rust_binary_search(arr, val, comp)
    return _py_binary_search(arr, val, comp)


def equal_range(arr: list, val: Any, comp: Callable[[Any, Any], bool] = None, use_rust: bool = True) -> tuple[int, int]:
    """
    Returns the range of elements equivalent to a given value.

    Args:
        arr: The sorted list to search.
        val: The value to search for.
        comp: Optional custom binary comparator Callable(a, b) defining custom less-than.
        use_rust: Whether to use the compiled Rust backend (default: True).

    Returns:
        A tuple (lower_bound_index, upper_bound_index) defining the range of equivalent elements.

    Time Complexity:
        O(log n)
    """
    if use_rust and RUST_AVAILABLE:
        return _rust_equal_range(arr, val, comp)
    return _py_equal_range(arr, val, comp)


__all__ = [
    'next_permutation', 'prev_permutation', 'nth_element', 'partition',
    'lower_bound', 'upper_bound', 'binary_search', 'equal_range',
    'RUST_AVAILABLE'
]
