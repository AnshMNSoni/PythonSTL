"""
Private implementation of Set data structure.

This module contains the internal implementation of a set
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar, List
from pythonstl.utility.iterator import SetIterator
from pythonstl.utility.avl_tree import AVLTree

T = TypeVar('T')


class _SetImpl:
    """
    Internal implementation of a set using an AVL Tree.

    This class should not be accessed directly by users.
    Use the facade class `stl_set` instead.
    """

    def __init__(self) -> None:
        """
        Initialize an empty set.

        Time Complexity:
            O(1)
        """
        self._data: AVLTree[T, None] = AVLTree()

    def insert(self, value: T) -> None:
        """
        Insert an element into the set.

        Args:
            value: The element to insert into the set.

        Time Complexity:
            O(log n)
        """
        self._data.add(value)

    def erase(self, value: T) -> None:
        """
        Remove an element from the set.

        Args:
            value: The element to remove from the set.

        Note:
            Does nothing if the element is not present (matches C++ STL behavior).

        Time Complexity:
            O(log n)
        """
        self._data.discard(value)

    def find(self, value: T) -> bool:
        """
        Check if an element exists in the set.

        Args:
            value: The element to search for.

        Returns:
            True if the element exists, False otherwise.

        Time Complexity:
            O(log n)
        """
        return value in self._data

    def empty(self) -> bool:
        """
        Check if the set is empty.

        Returns:
            True if the set is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return len(self._data) == 0

    def size(self) -> int:
        """
        Get the number of elements in the set.

        Returns:
            The number of elements in the set.

        Time Complexity:
            O(1)
        """
        return len(self._data)

    def begin(self) -> SetIterator:
        """
        Get iterator to the beginning of the set.

        Returns:
            Iterator pointing to the first element.

        Time Complexity:
            O(1)
        """
        return SetIterator(self._data)

    def end(self) -> SetIterator:
        """
        Get iterator to the end of the set.

        Returns:
            Iterator pointing past the last element.

        Time Complexity:
            O(1)
        """
        # Return an exhausted iterator
        it = SetIterator(set())
        return it

    def get_data(self) -> List[T]:
        """
        Get a copy of the internal data as a sorted list.

        Returns:
            Sorted list of the internal elements.

        Time Complexity:
            O(n) where n is the number of elements
        """
        return list(self._data)


__all__ = ['_SetImpl']
