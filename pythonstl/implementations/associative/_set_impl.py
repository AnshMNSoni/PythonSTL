"""
Private implementation of Set data structure.

This module contains the internal implementation of a set
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar, Set as PySet, Optional
from pythonstl.core.exceptions import EmptyContainerError
from pythonstl.core.iterator import SetIterator

T = TypeVar('T')


class _SetImpl:
    """
    Internal implementation of a set using Python's built-in set.
    
    This class should not be accessed directly by users.
    Use the facade class `stl_set` instead.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty set.
        
        Time Complexity:
            O(1)
        """
        self._data: PySet[T] = set()
    
    def insert(self, value: T) -> None:
        """
        Insert an element into the set.
        
        Args:
            value: The element to insert into the set.
            
        Time Complexity:
            O(1) average case
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
            O(1) average case
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
            O(1) average case
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
        
        Note: In Python sets, end() returns an exhausted iterator.
        
        Returns:
            Iterator pointing past the last element.
            
        Time Complexity:
            O(1)
        """
        # Return an exhausted iterator
        it = SetIterator(set())
        return it
    
    def get_data(self) -> PySet[T]:
        """
        Get a copy of the internal data for iteration.
        
        Returns:
            Copy of the internal data set.
            
        Time Complexity:
            O(n) where n is the number of elements
        """
        return self._data.copy()


__all__ = ['_SetImpl']
