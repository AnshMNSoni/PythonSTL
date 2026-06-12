"""
Queue facade class.

This module provides the public-facing queue class that users interact with.
"""

from typing import TypeVar
from copy import deepcopy
from pythonstl.core.exceptions import EmptyContainerError
from pythonstl.implementations.linear._queue_impl import _QueueImpl

try:
    from pythonstl._rust import RustQueue
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

T = TypeVar('T')


class queue:
    """
    A queue data structure following C++ STL semantics.

    This is a FIFO (First-In-First-Out) container adapter.

    Example:
        >>> from pythonstl import queue
        >>> q = queue()
        >>> q.push(10)
        >>> q.push(20)
        >>> q.front()
        10
        >>> len(q)
        2
        >>> bool(q)
        True
    """

    def __init__(self, use_rust: bool = True) -> None:
        """
        Initialize an empty queue.

        Time Complexity:
            O(1)
        """
        if use_rust and RUST_AVAILABLE:
            self._impl = RustQueue()
            self._is_rust = True
        else:
            self._impl = _QueueImpl()
            self._is_rust = False

    def push(self, value: T) -> None:
        """
        Add an element to the back of the queue.

        Args:
            value: The element to add to the queue.

        Time Complexity:
            O(1)
        """
        self._impl.push(value)

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
        self._impl.pop()

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
        return self._impl.front()

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
        return self._impl.back()

    def empty(self) -> bool:
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return self._impl.empty()

    def size(self) -> int:
        """
        Get the number of elements in the queue.

        Returns:
            The number of elements in the queue.

        Time Complexity:
            O(1)
        """
        return self._impl.size()

    def copy(self) -> 'queue':
        """
        Create a deep copy of the queue.

        Returns:
            A new queue with copied elements.

        Time Complexity:
            O(n) where n is the number of elements
        """
        new_queue = queue(use_rust=self._is_rust)
        if self._is_rust:
            new_queue._impl.set_data(self._impl.get_data())
        else:
            new_queue._impl._data = self._impl._data.copy()
        return new_queue

    # Python magic methods

    def __len__(self) -> int:
        """
        Get the number of elements (Python len() support).

        Returns:
            The number of elements in the queue.
        """
        return self.size()

    def __bool__(self) -> bool:
        """
        Check if queue is non-empty (Python bool() support).

        Returns:
            True if queue is non-empty, False otherwise.
        """
        return not self.empty()

    def __repr__(self) -> str:
        """
        Get string representation of the queue.

        Returns:
            String representation showing queue contents.
        """
        if self._is_rust:
            elements = [str(elem) for elem in self._impl.get_data()]
        else:
            elements = [str(elem) for elem in self._impl._data]
        return f"queue([{', '.join(elements)}])"

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another queue.

        Args:
            other: Another queue to compare with.

        Returns:
            True if queues are equal, False otherwise.
        """
        if not isinstance(other, queue):
            return False

        self_data = self._impl.get_data() if self._is_rust else self._impl._data
        other_data = other._impl.get_data() if other._is_rust else other._impl._data
        return self_data == other_data

    def __copy__(self) -> 'queue':
        """
        Support for copy.copy().

        Returns:
            A shallow copy of the queue.
        """
        return self.copy()

    def __deepcopy__(self, memo) -> 'queue':
        """
        Support for copy.deepcopy().

        Args:
            memo: Memoization dictionary for deepcopy.

        Returns:
            A deep copy of the queue.
        """
        new_queue = queue(use_rust=self._is_rust)
        if self._is_rust:
            new_data = deepcopy(self._impl.get_data(), memo)
            new_queue._impl.set_data(new_data)
        else:
            new_queue._impl._data = deepcopy(self._impl._data, memo)
        return new_queue


__all__ = ['queue']
