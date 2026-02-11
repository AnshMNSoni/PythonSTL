"""
Private implementation of Queue data structure.

This module contains the internal implementation of a queue
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar
from collections import deque
from pythonstl.core.exceptions import EmptyContainerError

T = TypeVar('T')


class _QueueImpl:
    """
    Internal implementation of a queue using collections.deque.

    This class should not be accessed directly by users.
    Use the facade class `queue` instead.
    """

    def __init__(self) -> None:
        """
        Initialize an empty queue.

        Time Complexity:
            O(1)
        """
        self._data: deque[T] = deque()

    def push(self, value: T) -> None:
        """
        Add an element to the back of the queue.

        Args:
            value: The element to add to the queue.

        Time Complexity:
            O(1)
        """
        self._data.append(value)

    def pop(self) -> None:
        """
        Remove the front element from the queue.

        Raises:
            EmptyContainerError: If the queue is empty.

        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("queue")
        self._data.popleft()

    def front(self) -> T:
        """
        Get the front element of the queue without removing it.

        Returns:
            The front element of the queue.

        Raises:
            EmptyContainerError: If the queue is empty.

        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("queue")
        return self._data[0]

    def back(self) -> T:
        """
        Get the back element of the queue without removing it.

        Returns:
            The back element of the queue.

        Raises:
            EmptyContainerError: If the queue is empty.

        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("queue")
        return self._data[-1]

    def empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return len(self._data) == 0

    def size(self) -> int:
        """
        Get the number of elements in the queue.

        Returns:
            The number of elements in the queue.

        Time Complexity:
            O(1)
        """
        return len(self._data)


__all__ = ['_QueueImpl']
