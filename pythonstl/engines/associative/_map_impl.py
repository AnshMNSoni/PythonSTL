"""
Private implementation of Map data structure.

This module contains the internal implementation of a map (key-value pairs)
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar, Dict
from pythonstl.utility.exceptions import KeyNotFoundError
from pythonstl.utility.iterator import MapIterator
from pythonstl.utility.avl_tree import AVLTree

K = TypeVar('K')
V = TypeVar('V')


class _MapImpl:
    """
    Internal implementation of a map using an AVL Tree.

    This class should not be accessed directly by users.
    Use the facade class `stl_map` instead.
    """

    def __init__(self) -> None:
        """
        Initialize an empty map.

        Time Complexity:
            O(1)
        """
        self._data: AVLTree[K, V] = AVLTree()

    def insert(self, key: K, value: V) -> None:
        """
        Insert a key-value pair into the map.

        Args:
            key: The key to insert.
            value: The value associated with the key.

        Note:
            If the key already exists, the value is updated.

        Time Complexity:
            O(log n)
        """
        self._data[key] = value

    def erase(self, key: K) -> None:
        """
        Remove a key-value pair from the map.

        Args:
            key: The key to remove.

        Note:
            Does nothing if the key is not present (matches C++ STL behavior).

        Time Complexity:
            O(log n)
        """
        self._data.discard(key)

    def find(self, key: K) -> bool:
        """
        Check if a key exists in the map.

        Args:
            key: The key to search for.

        Returns:
            True if the key exists, False otherwise.

        Time Complexity:
            O(log n)
        """
        return key in self._data

    def at(self, key: K) -> V:
        """
        Access the value associated with a key.

        Args:
            key: The key to access.

        Returns:
            The value associated with the key.

        Raises:
            KeyNotFoundError: If the key does not exist.

        Time Complexity:
            O(log n)
        """
        try:
            return self._data[key]
        except KeyError:
            raise KeyNotFoundError(key)

    def empty(self) -> bool:
        """
        Check if the map is empty.

        Returns:
            True if the map is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return len(self._data) == 0

    def size(self) -> int:
        """
        Get the number of key-value pairs in the map.

        Returns:
            The number of key-value pairs in the map.

        Time Complexity:
            O(1)
        """
        return len(self._data)

    def begin(self) -> MapIterator:
        """
        Get iterator to the beginning of the map.

        Returns:
            Iterator pointing to the first key-value pair.

        Time Complexity:
            O(1)
        """
        return MapIterator(self._data)

    def end(self) -> MapIterator:
        """
        Get iterator to the end of the map.

        Returns:
            Iterator pointing past the last key-value pair.

        Time Complexity:
            O(1)
        """
        # Return an exhausted iterator
        it = MapIterator({})
        return it

    def get_data(self) -> Dict[K, V]:
        """
        Get a copy of the internal data as a sorted dictionary.

        Returns:
            Sorted copy of the internal data dict.

        Time Complexity:
            O(n) where n is the number of key-value pairs
        """
        return dict(self._data.items())


__all__ = ['_MapImpl']
