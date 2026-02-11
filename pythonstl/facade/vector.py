"""
Vector facade class.

This module provides the public-facing vector class that users interact with.
"""

from typing import TypeVar, Iterator as TypingIterator
from copy import deepcopy
from pythonstl.implementations.linear._vector_impl import _VectorImpl
from pythonstl.core.iterator import VectorIterator, VectorReverseIterator

T = TypeVar('T')


class vector:
    """
    A dynamic array (vector) data structure following C++ STL semantics.

    This is a sequence container with dynamic size.

    Example:
        >>> from pythonstl import vector
        >>> v = vector()
        >>> v.push_back(10)
        >>> v.push_back(20)
        >>> v.at(0)
        10
        >>> len(v)
        2
        >>> 10 in v
        True
    """

    def __init__(self) -> None:
        """
        Initialize an empty vector.

        Time Complexity:
            O(1)
        """
        self._impl = _VectorImpl()

    def push_back(self, value: T) -> None:
        """
        Add an element to the end of the vector.

        Args:
            value: The element to add to the vector.

        Time Complexity:
            O(1) amortized
        """
        self._impl.push_back(value)

    def pop_back(self) -> None:
        """
        Remove the last element from the vector.

        Raises:
            EmptyContainerError: If the vector is empty.

        Time Complexity:
            O(1)
        """
        self._impl.pop_back()

    def at(self, index: int) -> T:
        """
        Access element at specified index with bounds checking.

        Args:
            index: The index of the element to access.

        Returns:
            The element at the specified index.

        Raises:
            OutOfRangeError: If index is out of bounds.

        Time Complexity:
            O(1)
        """
        return self._impl.at(index)

    def insert(self, position: int, value: T) -> None:
        """
        Insert an element at the specified position.

        Args:
            position: The position to insert the element.
            value: The element to insert.

        Raises:
            OutOfRangeError: If position is out of bounds.

        Time Complexity:
            O(n) where n is the number of elements after position
        """
        self._impl.insert(position, value)

    def erase(self, position: int) -> None:
        """
        Remove the element at the specified position.

        Args:
            position: The position of the element to remove.

        Raises:
            OutOfRangeError: If position is out of bounds.

        Time Complexity:
            O(n) where n is the number of elements after position
        """
        self._impl.erase(position)

    def clear(self) -> None:
        """
        Remove all elements from the vector.

        Time Complexity:
            O(n) where n is the number of elements
        """
        self._impl.clear()

    def reserve(self, new_capacity: int) -> None:
        """
        Reserve capacity for the vector.

        Pre-allocates memory to avoid reallocation during growth.
        Does not change the size of the vector.

        Args:
            new_capacity: The new capacity to reserve.

        Time Complexity:
            O(1)
        """
        self._impl.reserve(new_capacity)

    def shrink_to_fit(self) -> None:
        """
        Reduce capacity to match the current size.

        Frees unused capacity to save memory.

        Time Complexity:
            O(1)
        """
        self._impl.shrink_to_fit()

    def begin(self) -> VectorIterator:
        """
        Get iterator to the beginning of the vector.

        Returns:
            Iterator pointing to the first element.

        Time Complexity:
            O(1)
        """
        return self._impl.begin()

    def end(self) -> VectorIterator:
        """
        Get iterator to the end of the vector.

        Returns:
            Iterator pointing past the last element.

        Time Complexity:
            O(1)
        """
        return self._impl.end()

    def rbegin(self) -> VectorReverseIterator:
        """
        Get reverse iterator to the end of the vector.

        Returns:
            Reverse iterator pointing to the last element.

        Time Complexity:
            O(1)
        """
        return self._impl.rbegin()

    def rend(self) -> VectorReverseIterator:
        """
        Get reverse iterator to the beginning of the vector.

        Returns:
            Reverse iterator pointing before the first element.

        Time Complexity:
            O(1)
        """
        return self._impl.rend()

    def size(self) -> int:
        """
        Get the number of elements in the vector.

        Returns:
            The number of elements in the vector.

        Time Complexity:
            O(1)
        """
        return self._impl.size()

    def capacity(self) -> int:
        """
        Get the current capacity of the vector.

        Returns:
            The current capacity of the vector.

        Time Complexity:
            O(1)
        """
        return self._impl.capacity()

    def empty(self) -> bool:
        """
        Check if the vector is empty.

        Returns:
            True if the vector is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return self._impl.empty()

    def copy(self) -> 'vector':
        """
        Create a deep copy of the vector.

        Returns:
            A new vector with copied elements.

        Time Complexity:
            O(n) where n is the number of elements
        """
        new_vector = vector()
        for i in range(self.size()):
            new_vector.push_back(self.at(i))
        return new_vector

    # Python magic methods

    def __len__(self) -> int:
        """
        Get the number of elements (Python len() support).

        Returns:
            The number of elements in the vector.
        """
        return self.size()

    def __bool__(self) -> bool:
        """
        Check if vector is non-empty (Python bool() support).

        Returns:
            True if vector is non-empty, False otherwise.
        """
        return not self.empty()

    def __contains__(self, value: T) -> bool:
        """
        Check if value exists in vector (Python 'in' operator support).

        Args:
            value: The value to search for.

        Returns:
            True if value exists, False otherwise.

        Time Complexity:
            O(n) where n is the number of elements
        """
        for i in range(self.size()):
            if self.at(i) == value:
                return True
        return False

    def __repr__(self) -> str:
        """
        Get string representation of the vector.

        Returns:
            String representation showing all elements.
        """
        elements = [str(self.at(i)) for i in range(self.size())]
        return f"vector([{', '.join(elements)}])"

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another vector.

        Args:
            other: Another vector to compare with.

        Returns:
            True if vectors are equal, False otherwise.
        """
        if not isinstance(other, vector):
            return False
        if self.size() != other.size():
            return False
        for i in range(self.size()):
            if self.at(i) != other.at(i):
                return False
        return True

    def __lt__(self, other: 'vector') -> bool:
        """
        Lexicographic less-than comparison.

        Args:
            other: Another vector to compare with.

        Returns:
            True if this vector is lexicographically less than other.
        """
        min_size = min(self.size(), other.size())
        for i in range(min_size):
            if self.at(i) < other.at(i):
                return True
            elif self.at(i) > other.at(i):
                return False
        return self.size() < other.size()

    def __iter__(self) -> TypingIterator[T]:
        """
        Get Python iterator for the vector.

        Returns:
            Iterator over vector elements.
        """
        return iter(self._impl.get_data())

    def __copy__(self) -> 'vector':
        """
        Support for copy.copy().

        Returns:
            A shallow copy of the vector.
        """
        return self.copy()

    def __deepcopy__(self, memo) -> 'vector':
        """
        Support for copy.deepcopy().

        Args:
            memo: Memoization dictionary for deepcopy.

        Returns:
            A deep copy of the vector.
        """
        new_vector = vector()
        for i in range(self.size()):
            new_vector.push_back(deepcopy(self.at(i), memo))
        return new_vector


__all__ = ['vector']
