"""
Private implementation of Priority Queue data structure.

This module contains the internal implementation of a priority queue
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar, List
import heapq
from pythonstl.utility.exceptions import EmptyContainerError

T = TypeVar('T')


class _PriorityQueueImpl:
    """
    Internal implementation of a priority queue using heapq.

    This class should not be accessed directly by users.
    Use the facade class `priority_queue` instead.

    Note:
        Python's heapq implements a min-heap. We support both min and max heaps
        through the comparator parameter.
    """

    def __init__(self, comparator: str = "max") -> None:
        """
        Initialize an empty priority queue.

        Args:
            comparator: Either "max" for max-heap (default, matches C++ STL)
                       or "min" for min-heap.

        Time Complexity:
            O(1)
        """
        self._data: List[T] = []
        self._comparator = comparator
        if comparator not in ["max", "min"]:
            raise ValueError("comparator must be 'max' or 'min'")

    def push(self, value: T) -> None:
        """
        Insert an element into the priority queue.

        Args:
            value: The element to insert.

        Time Complexity:
            O(log n) where n is the number of elements
        """
        if self._comparator == "max":
            # Negate for max-heap behavior
            heapq.heappush(self._data, -value if isinstance(value, (int, float)) else value)
        else:
            heapq.heappush(self._data, value)

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
        heapq.heappop(self._data)

    def top(self) -> T:
        """
        Get the top element of the priority queue without removing it.

        Returns:
            The top element (highest priority).

        Raises:
            EmptyContainerError: If the priority queue is empty.

        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("priority_queue")
        top_value = self._data[0]
        if self._comparator == "max" and isinstance(top_value, (int, float)):
            return -top_value
        return top_value

    def empty(self) -> bool:
        """
        Check if the priority queue is empty.

        Returns:
            True if the priority queue is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return len(self._data) == 0

    def size(self) -> int:
        """
        Get the number of elements in the priority queue.

        Returns:
            The number of elements in the priority queue.

        Time Complexity:
            O(1)
        """
        return len(self._data)


__all__ = ['_PriorityQueueImpl']
