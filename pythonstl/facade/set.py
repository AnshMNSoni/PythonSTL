"""
Set facade class.

This module provides the public-facing set class that users interact with.
"""

from typing import TypeVar, Iterator as TypingIterator
from copy import deepcopy
from pythonstl.implementations.associative._set_impl import _SetImpl
from pythonstl.core.iterator import SetIterator

try:
    from pythonstl._rust import RustSet
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

T = TypeVar('T')


class stl_set:
    """
    A set data structure following C++ STL semantics.

    This is an associative container that stores unique elements.
    Named 'stl_set' to avoid conflict with Python's built-in set.

    Example:
        >>> from pythonstl import stl_set
        >>> s = stl_set()
        >>> s.insert(10)
        >>> s.insert(20)
        >>> s.find(10)
        True
        >>> 10 in s
        True
        >>> len(s)
        2
    """

    def __init__(self, use_rust: bool = True) -> None:
        """
        Initialize an empty set.

        Time Complexity:
            O(1)
        """
        if use_rust and RUST_AVAILABLE:
            self._impl = RustSet()
            self._is_rust = True
        else:
            self._impl = _SetImpl()
            self._is_rust = False

    def insert(self, value: T) -> None:
        """
        Insert an element into the set.

        Args:
            value: The element to insert into the set.

        Time Complexity:
            O(1) average case
        """
        self._impl.insert(value)

    def erase(self, value: T) -> None:
        """
        Remove an element from the set.

        Args:
            value: The element to remove from the set.

        Note:
            Does nothing if the element is not present (matches C++ STL behavior).

        Time Complexity:
            O(1) average case
        """
        self._impl.erase(value)

    def find(self, value: T) -> bool:
        """
        Check if an element exists in the set.

        Args:
            value: The element to search for.

        Returns:
            True if the element exists, False otherwise.

        Time Complexity:
            O(1) average case
        """
        return self._impl.find(value)

    def empty(self) -> bool:
        """
        Check if the set is empty.

        Returns:
            True if the set is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return self._impl.empty()

    def size(self) -> int:
        """
        Get the number of elements in the set.

        Returns:
            The number of elements in the set.

        Time Complexity:
            O(1)
        """
        return self._impl.size()

    def begin(self) -> SetIterator:
        """
        Get iterator to the beginning of the set.

        Returns:
            Iterator pointing to the first element.

        Time Complexity:
            O(1)
        """
        data = self._impl.get_data() if self._is_rust else self._impl._data
        return SetIterator(data)

    def end(self) -> SetIterator:
        """
        Get iterator to the end of the set.

        Returns:
            Iterator pointing past the last element.

        Time Complexity:
            O(1)
        """
        # Return an exhausted iterator
        return SetIterator(set())

    def copy(self) -> 'stl_set':
        """
        Create a deep copy of the set.

        Returns:
            A new set with copied elements.

        Time Complexity:
            O(n) where n is the number of elements
        """
        new_set = stl_set(use_rust=self._is_rust)
        if self._is_rust:
            new_set._impl.set_data(self._impl.get_data())
        else:
            new_set._impl._data = self._impl._data.copy()
        return new_set

    # Python magic methods

    def __len__(self) -> int:
        """
        Get the number of elements (Python len() support).

        Returns:
            The number of elements in the set.
        """
        return self.size()

    def __bool__(self) -> bool:
        """
        Check if set is non-empty (Python bool() support).

        Returns:
            True if set is non-empty, False otherwise.
        """
        return not self.empty()

    def __contains__(self, value: T) -> bool:
        """
        Check if value exists in set (Python 'in' operator support).

        Args:
            value: The value to search for.

        Returns:
            True if value exists, False otherwise.

        Time Complexity:
            O(1) average case
        """
        return self.find(value)

    def __repr__(self) -> str:
        """
        Get string representation of the set.

        Returns:
            String representation showing all elements.
        """
        elements = [str(elem) for elem in self]
        return f"stl_set({{{', '.join(elements)}}})"

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another set.

        Args:
            other: Another set to compare with.

        Returns:
            True if sets are equal, False otherwise.
        """
        if not isinstance(other, stl_set):
            return False
        
        self_data = self._impl.get_data() if self._is_rust else self._impl._data
        other_data = other._impl.get_data() if other._is_rust else other._impl._data
        
        # BTreeSet elements are sorted, so direct list equality works for sorted comparison
        if self._is_rust and other._is_rust:
            return self_data == other_data
            
        return set(self_data) == set(other_data)

    def __iter__(self) -> TypingIterator[T]:
        """
        Get Python iterator for the set.

        Returns:
            Iterator over set elements.
        """
        if self._is_rust:
            return iter(self._impl.get_data())
        return iter(self._impl.get_data())

    def __copy__(self) -> 'stl_set':
        """
        Support for copy.copy().

        Returns:
            A shallow copy of the set.
        """
        return self.copy()

    def __deepcopy__(self, memo) -> 'stl_set':
        """
        Support for copy.deepcopy().

        Args:
            memo: Memoization dictionary for deepcopy.

        Returns:
            A deep copy of the set.
        """
        new_set = stl_set(use_rust=self._is_rust)
        if self._is_rust:
            new_data = deepcopy(self._impl.get_data(), memo)
            new_set._impl.set_data(new_data)
        else:
            new_set._impl._data = deepcopy(self._impl._data, memo)
        return new_set



__all__ = ['stl_set']
