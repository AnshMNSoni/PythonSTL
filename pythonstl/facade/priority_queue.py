"""
Priority Queue facade class.

This module provides the public-facing priority_queue class that users interact with.
"""

from typing import TypeVar
from copy import deepcopy
from pythonstl.core.exceptions import EmptyContainerError
from pythonstl.implementations.heaps._priority_queue_impl import _PriorityQueueImpl

try:
    from pythonstl._rust import RustPriorityQueue
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

T = TypeVar('T')


class priority_queue:
    """
    A priority queue data structure following C++ STL semantics.

    This is a container adapter that provides constant time lookup of the
    largest (by default) or smallest element, at the expense of logarithmic
    insertion and extraction.

    Example:
        >>> from pythonstl import priority_queue
        >>> pq = priority_queue()  # max-heap by default
        >>> pq.push(10)
        >>> pq.push(30)
        >>> pq.push(20)
        >>> pq.top()
        30
        >>> len(pq)
        3
        >>>
        >>> pq_min = priority_queue(comparator="min")  # min-heap
        >>> pq_min.push(10)
        >>> pq_min.push(30)
        >>> pq_min.push(20)
        >>> pq_min.top()
        10
    """

    def __init__(self, comparator: str = "max", use_rust: bool = True) -> None:
        """
        Initialize an empty priority queue.

        Args:
            comparator: Either "max" for max-heap (default, matches C++ STL)
                       or "min" for min-heap.

        Time Complexity:
            O(1)
        """
        if use_rust and RUST_AVAILABLE:
            self._impl = RustPriorityQueue(comparator)
            self._is_rust = True
        else:
            self._impl = _PriorityQueueImpl(comparator)
            self._is_rust = False
        self._comparator = comparator

    def push(self, value: T) -> None:
        """
        Insert an element into the priority queue.

        Args:
            value: The element to insert.

        Time Complexity:
            O(log n) where n is the number of elements
        """
        self._impl.push(value)

    def pop(self) -> None:
        """
        Remove the top element from the priority queue.

        Raises:
            EmptyContainerError: If the priority queue is empty.

        Time Complexity:
            O(log n) where n is the number of elements
        """
        if self.empty():
            raise EmptyContainerError("priority_queue")
        self._impl.pop()

    def top(self) -> T:
        """
        Get the top element of the priority queue without removing it.

        Returns:
            The top element (highest priority for max-heap, lowest for min-heap).

        Raises:
            EmptyContainerError: If the priority queue is empty.

        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("priority_queue")
        return self._impl.top()

    def empty(self) -> bool:
        """
        Check if the priority queue is empty.

        Returns:
            True if the priority queue is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return self._impl.empty()

    def size(self) -> int:
        """
        Get the number of elements in the priority queue.

        Returns:
            The number of elements in the priority queue.

        Time Complexity:
            O(1)
        """
        return self._impl.size()

    def copy(self) -> 'priority_queue':
        """
        Create a deep copy of the priority queue.

        Returns:
            A new priority queue with copied elements.

        Time Complexity:
            O(n) where n is the number of elements
        """
        new_pq = priority_queue(self._comparator, use_rust=self._is_rust)
        if self._is_rust:
            new_pq._impl.set_data(self._impl.get_data())
        else:
            new_pq._impl._data = self._impl._data.copy()
        return new_pq

    # Python magic methods

    def __len__(self) -> int:
        """
        Get the number of elements (Python len() support).

        Returns:
            The number of elements in the priority queue.
        """
        return self.size()

    def __bool__(self) -> bool:
        """
        Check if priority queue is non-empty (Python bool() support).

        Returns:
            True if priority queue is non-empty, False otherwise.
        """
        return not self.empty()

    def __repr__(self) -> str:
        """
        Get string representation of the priority queue.

        Returns:
            String representation showing heap type and size.
        """
        return f"priority_queue(comparator='{self._comparator}', size={self.size()})"

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another priority queue.

        Args:
            other: Another priority queue to compare with.

        Returns:
            True if priority queues are equal, False otherwise.
        """
        if not isinstance(other, priority_queue):
            return False
        if self._comparator != other._comparator:
            return False

        self_data = self._impl.get_data() if self._is_rust else self._impl._data
        other_data = other._impl.get_data() if other._is_rust else other._impl._data
        return self_data == other_data

    def __copy__(self) -> 'priority_queue':
        """
        Support for copy.copy().

        Returns:
            A shallow copy of the priority queue.
        """
        return self.copy()

    def __deepcopy__(self, memo) -> 'priority_queue':
        """
        Support for copy.deepcopy().

        Args:
            memo: Memoization dictionary for deepcopy.

        Returns:
            A deep copy of the priority queue.
        """
        new_pq = priority_queue(self._comparator, use_rust=self._is_rust)
        if self._is_rust:
            new_data = deepcopy(self._impl.get_data(), memo)
            new_pq._impl.set_data(new_data)
        else:
            new_pq._impl._data = deepcopy(self._impl._data, memo)
        return new_pq


__all__ = ['priority_queue']
