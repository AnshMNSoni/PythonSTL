"""
Map facade class.

This module provides the public-facing map class that users interact with.
"""

from typing import TypeVar, Iterator as TypingIterator, Tuple
from copy import deepcopy
from pythonstl.core.exceptions import KeyNotFoundError
from pythonstl.implementations.associative._map_impl import _MapImpl
from pythonstl.core.iterator import MapIterator

try:
    from pythonstl._rust import RustMap
    RUST_AVAILABLE = True
except ImportError:
    RUST_AVAILABLE = False

K = TypeVar('K')
V = TypeVar('V')


class stl_map:
    """
    A map data structure following C++ STL semantics.

    This is an associative container that stores key-value pairs.
    Named 'stl_map' to avoid potential conflicts.

    Example:
        >>> from pythonstl import stl_map
        >>> m = stl_map()
        >>> m.insert("key1", 100)
        >>> m.insert("key2", 200)
        >>> m.at("key1")
        100
        >>> "key1" in m
        True
        >>> len(m)
        2
    """

    def __init__(self, use_rust: bool = True) -> None:
        """
        Initialize an empty map.

        Time Complexity:
            O(1)
        """
        if use_rust and RUST_AVAILABLE:
            self._impl = RustMap()
            self._is_rust = True
        else:
            self._impl = _MapImpl()
            self._is_rust = False

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
        self._impl.insert(key, value)

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
        self._impl.erase(key)

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
        return self._impl.find(key)

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
        if not self.find(key):
            raise KeyNotFoundError(key)
        if self._is_rust:
            return self._impl.at(key)
        return self._impl.at(key)

    def empty(self) -> bool:
        """
        Check if the map is empty.

        Returns:
            True if the map is empty, False otherwise.

        Time Complexity:
            O(1)
        """
        return self._impl.empty()

    def size(self) -> int:
        """
        Get the number of key-value pairs in the map.

        Returns:
            The number of key-value pairs in the map.

        Time Complexity:
            O(1)
        """
        return self._impl.size()

    def begin(self) -> MapIterator:
        """
        Get iterator to the beginning of the map.

        Returns:
            Iterator pointing to the first key-value pair.

        Time Complexity:
            O(1)
        """
        if self._is_rust:
            return MapIterator(dict(self._impl.get_data()))
        return self._impl.begin()

    def end(self) -> MapIterator:
        """
        Get iterator to the end of the map.

        Returns:
            Iterator pointing past the last key-value pair.

        Time Complexity:
            O(1)
        """
        if self._is_rust:
            return MapIterator({})
        return self._impl.end()

    def copy(self) -> 'stl_map':
        """
        Create a deep copy of the map.

        Returns:
            A new map with copied key-value pairs.

        Time Complexity:
            O(n) where n is the number of key-value pairs
        """
        new_map = stl_map(use_rust=self._is_rust)
        if self._is_rust:
            new_map._impl.set_data(self._impl.get_data())
        else:
            new_map._impl._data = self._impl._data.copy()
        return new_map

    # Python magic methods

    def __len__(self) -> int:
        """
        Get the number of key-value pairs (Python len() support).

        Returns:
            The number of key-value pairs in the map.
        """
        return self.size()

    def __bool__(self) -> bool:
        """
        Check if map is non-empty (Python bool() support).

        Returns:
            True if map is non-empty, False otherwise.
        """
        return not self.empty()

    def __contains__(self, key: K) -> bool:
        """
        Check if key exists in map (Python 'in' operator support).

        Args:
            key: The key to search for.

        Returns:
            True if key exists, False otherwise.

        Time Complexity:
            O(1) average case
        """
        return self.find(key)

    def __repr__(self) -> str:
        """
        Get string representation of the map.

        Returns:
            String representation showing all key-value pairs.
        """
        pairs = [f"{k}: {v}" for k, v in self]
        return f"stl_map({{{', '.join(pairs)}}})"

    def __eq__(self, other: object) -> bool:
        """
        Check equality with another map.

        Args:
            other: Another map to compare with.

        Returns:
            True if maps are equal, False otherwise.
        """
        if not isinstance(other, stl_map):
            return False

        self_data = dict(self._impl.get_data()) if self._is_rust else self._impl._data
        other_data = dict(other._impl.get_data()) if other._is_rust else other._impl._data
        return self_data == other_data

    def __iter__(self) -> TypingIterator[Tuple[K, V]]:
        """
        Get Python iterator for the map.

        Returns:
            Iterator over key-value pairs as tuples.
        """
        if self._is_rust:
            return iter(self._impl.get_data())
        return iter(self._impl.get_data().items())

    def __copy__(self) -> 'stl_map':
        """
        Support for copy.copy().

        Returns:
            A shallow copy of the map.
        """
        return self.copy()

    def __deepcopy__(self, memo) -> 'stl_map':
        """
        Support for copy.deepcopy().

        Args:
            memo: Memoization dictionary for deepcopy.

        Returns:
            A deep copy of the map.
        """
        new_map = stl_map(use_rust=self._is_rust)
        if self._is_rust:
            new_pairs = []
            for k, v in self._impl.get_data():
                new_pairs.append((deepcopy(k, memo), deepcopy(v, memo)))
            new_map._impl.set_data(new_pairs)
        else:
            new_map._impl._data = deepcopy(self._impl._data, memo)
        return new_map


__all__ = ['stl_map']
