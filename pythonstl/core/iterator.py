"""
Iterator classes for pystl containers.

This module provides iterator support for STL-style containers,
enabling both C++ STL-style iteration and Python iteration protocols.
"""

from typing import TypeVar, Generic, List, Any
from abc import ABC, abstractmethod

T = TypeVar('T')


class Iterator(ABC, Generic[T]):
    """
    Abstract base class for iterators.
    
    Provides the foundation for both forward and reverse iterators.
    """
    
    @abstractmethod
    def __next__(self) -> T:
        """Get the next element."""
        pass
    
    @abstractmethod
    def __iter__(self):
        """Return the iterator itself."""
        pass


class VectorIterator(Iterator[T]):
    """
    Forward iterator for vector.
    
    This iterator traverses the vector from beginning to end.
    """
    
    def __init__(self, data: List[T], index: int = 0) -> None:
        """
        Initialize vector iterator.
        
        Args:
            data: Reference to the vector's internal data
            index: Starting position
        """
        self._data = data
        self._index = index
    
    def __next__(self) -> T:
        """
        Get the next element.
        
        Returns:
            The next element in the vector.
            
        Raises:
            StopIteration: When iteration is complete.
        """
        if self._index >= len(self._data):
            raise StopIteration
        value = self._data[self._index]
        self._index += 1
        return value
    
    def __iter__(self):
        """Return the iterator itself."""
        return self


class VectorReverseIterator(Iterator[T]):
    """
    Reverse iterator for vector.
    
    This iterator traverses the vector from end to beginning.
    """
    
    def __init__(self, data: List[T], index: int = -1) -> None:
        """
        Initialize reverse vector iterator.
        
        Args:
            data: Reference to the vector's internal data
            index: Starting position (default: last element)
        """
        self._data = data
        if index == -1:
            self._index = len(data) - 1
        else:
            self._index = index
    
    def __next__(self) -> T:
        """
        Get the next element (in reverse order).
        
        Returns:
            The next element in reverse order.
            
        Raises:
            StopIteration: When iteration is complete.
        """
        if self._index < 0:
            raise StopIteration
        value = self._data[self._index]
        self._index -= 1
        return value
    
    def __iter__(self):
        """Return the iterator itself."""
        return self


class SetIterator(Iterator[T]):
    """
    Iterator for set.
    
    This iterator traverses the set elements.
    Note: Order is not guaranteed (matches Python set behavior).
    """
    
    def __init__(self, data: set) -> None:
        """
        Initialize set iterator.
        
        Args:
            data: Reference to the set's internal data
        """
        self._iterator = iter(data)
    
    def __next__(self) -> T:
        """
        Get the next element.
        
        Returns:
            The next element in the set.
            
        Raises:
            StopIteration: When iteration is complete.
        """
        return next(self._iterator)
    
    def __iter__(self):
        """Return the iterator itself."""
        return self


class MapIterator(Iterator):
    """
    Iterator for map.
    
    This iterator traverses the map's key-value pairs.
    Returns tuples of (key, value).
    """
    
    def __init__(self, data: dict) -> None:
        """
        Initialize map iterator.
        
        Args:
            data: Reference to the map's internal data
        """
        self._iterator = iter(data.items())
    
    def __next__(self):
        """
        Get the next key-value pair.
        
        Returns:
            Tuple of (key, value).
            
        Raises:
            StopIteration: When iteration is complete.
        """
        return next(self._iterator)
    
    def __iter__(self):
        """Return the iterator itself."""
        return self


__all__ = [
    'Iterator',
    'VectorIterator',
    'VectorReverseIterator',
    'SetIterator',
    'MapIterator'
]
