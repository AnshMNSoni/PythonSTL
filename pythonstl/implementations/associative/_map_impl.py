"""
Private implementation of Map data structure.

This module contains the internal implementation of a map (key-value pairs)
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar, Dict
from pythonstl.core.exceptions import KeyNotFoundError
from pythonstl.core.iterator import MapIterator

K = TypeVar('K')
V = TypeVar('V')


class _MapImpl:
    """
    Internal implementation of a map using Python's built-in dict.

    This class should not be accessed directly by users.
    Use the facade class `stl_map` instead.
    """

    def __init__(self) -> None:
        """
        Initialize an empty map.

        Time Complexity:
            O(1)
        """
        self._data: Dict[K, V] = {}

    def insert(self, key: K, value: V) -> None:
        """
        Insert a key-value pair into the map.

        Args:
            key: The key to insert.
            value: The value associated with the key.

        Note:
            If the key already exists, the value is updated.

        Time Complexity:
            O(1) average case
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
            O(1) average case
        """
        self._data.pop(key, None)

    def find(self, key: K) -> bool:
        """
        Check if a key exists in the map.

        Args:
            key: The key to search for.

        Returns:
            True if the key exists, False otherwise.

        Time Complexity:
            O(1) average case
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
            O(1) average case
        """
        if key not in self._data:
            raise KeyNotFoundError(key)
        return self._data[key]

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

        Note: In Python dicts, end() returns an exhausted iterator.

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
        Get a copy of the internal data for iteration.

        Returns:
            Copy of the internal data dict.

        Time Complexity:
            O(n) where n is the number of key-value pairs
        """
        return self._data.copy()


__all__ = ['_MapImpl']
