"""
Private implementation of Vector data structure.

This module contains the internal implementation of a dynamic array (vector)
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar, List
from pythonstl.core.exceptions import EmptyContainerError, OutOfRangeError
from pythonstl.core.iterator import VectorIterator, VectorReverseIterator

T = TypeVar('T')


class _VectorImpl:
    """
    Internal implementation of a vector using Python list with capacity management.
    
    This class should not be accessed directly by users.
    Use the facade class `vector` instead.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty vector.
        
        Time Complexity:
            O(1)
        """
        self._data: List[T] = []
        self._capacity: int = 0
    
    def push_back(self, value: T) -> None:
        """
        Add an element to the end of the vector.
        
        Args:
            value: The element to add to the vector.
            
        Time Complexity:
            O(1) amortized
        """
        self._data.append(value)
        if len(self._data) > self._capacity:
            self._capacity = max(1, self._capacity * 2)
    
    def pop_back(self) -> None:
        """
        Remove the last element from the vector.
        
        Raises:
            EmptyContainerError: If the vector is empty.
            
        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("vector")
        self._data.pop()
    
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
        if index < 0 or index >= len(self._data):
            raise OutOfRangeError(index, len(self._data))
        return self._data[index]
    
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
        if position < 0 or position > len(self._data):
            raise OutOfRangeError(position, len(self._data))
        self._data.insert(position, value)
        if len(self._data) > self._capacity:
            self._capacity = max(1, self._capacity * 2)
    
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
        if position < 0 or position >= len(self._data):
            raise OutOfRangeError(position, len(self._data))
        self._data.pop(position)
    
    def clear(self) -> None:
        """
        Remove all elements from the vector.
        
        Time Complexity:
            O(n) where n is the number of elements
        """
        self._data.clear()
    
    def reserve(self, new_capacity: int) -> None:
        """
        Reserve capacity for the vector.
        
        Pre-allocates memory to avoid reallocation during growth.
        Does not change the size of the vector.
        
        Args:
            new_capacity: The new capacity to reserve.
            
        Time Complexity:
            O(1) - only updates capacity tracking
        """
        if new_capacity > self._capacity:
            self._capacity = new_capacity
    
    def shrink_to_fit(self) -> None:
        """
        Reduce capacity to match the current size.
        
        Frees unused capacity to save memory.
        
        Time Complexity:
            O(1) - only updates capacity tracking
        """
        self._capacity = len(self._data)
    
    def begin(self) -> VectorIterator:
        """
        Get iterator to the beginning of the vector.
        
        Returns:
            Iterator pointing to the first element.
            
        Time Complexity:
            O(1)
        """
        return VectorIterator(self._data, 0)
    
    def end(self) -> VectorIterator:
        """
        Get iterator to the end of the vector.
        
        Returns:
            Iterator pointing past the last element.
            
        Time Complexity:
            O(1)
        """
        return VectorIterator(self._data, len(self._data))
    
    def rbegin(self) -> VectorReverseIterator:
        """
        Get reverse iterator to the end of the vector.
        
        Returns:
            Reverse iterator pointing to the last element.
            
        Time Complexity:
            O(1)
        """
        return VectorReverseIterator(self._data)
    
    def rend(self) -> VectorReverseIterator:
        """
        Get reverse iterator to the beginning of the vector.
        
        Returns:
            Reverse iterator pointing before the first element.
            
        Time Complexity:
            O(1)
        """
        return VectorReverseIterator(self._data, -1)
    
    def get_data(self) -> List[T]:
        """
        Get a copy of the internal data for iteration.
        
        Returns:
            Copy of the internal data list.
            
        Time Complexity:
            O(n) where n is the number of elements
        """
        return self._data.copy()
    
    def size(self) -> int:
        """
        Get the number of elements in the vector.
        
        Returns:
            The number of elements in the vector.
            
        Time Complexity:
            O(1)
        """
        return len(self._data)
    
    def capacity(self) -> int:
        """
        Get the current capacity of the vector.
        
        Returns:
            The current capacity of the vector.
            
        Time Complexity:
            O(1)
        """
        return self._capacity
    
    def empty(self) -> bool:
        """
        Check if the vector is empty.
        
        Returns:
            True if the vector is empty, False otherwise.
            
        Time Complexity:
            O(1)
        """
        return len(self._data) == 0


__all__ = ['_VectorImpl']
