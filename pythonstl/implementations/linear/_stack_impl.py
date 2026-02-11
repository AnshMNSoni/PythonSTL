"""
Private implementation of Stack data structure.

This module contains the internal implementation of a stack
following C++ STL semantics. Users should not access this directly.
"""

from typing import TypeVar, List, Optional
from pythonstl.core.exceptions import EmptyContainerError

T = TypeVar('T')


class _StackImpl:
    """
    Internal implementation of a stack using Python list.
    
    This class should not be accessed directly by users.
    Use the facade class `stack` instead.
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        
        Time Complexity:
            O(1)
        """
        self._data: List[T] = []
    
    def push(self, value: T) -> None:
        """
        Push an element onto the stack.
        
        Args:
            value: The element to push onto the stack.
            
        Time Complexity:
            O(1) amortized
        """
        self._data.append(value)
    
    def pop(self) -> None:
        """
        Remove the top element from the stack.
        
        Raises:
            EmptyContainerError: If the stack is empty.
            
        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("stack")
        self._data.pop()
    
    def top(self) -> T:
        """
        Get the top element of the stack without removing it.
        
        Returns:
            The top element of the stack.
            
        Raises:
            EmptyContainerError: If the stack is empty.
            
        Time Complexity:
            O(1)
        """
        if self.empty():
            raise EmptyContainerError("stack")
        return self._data[-1]
    
    def empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
            
        Time Complexity:
            O(1)
        """
        return len(self._data) == 0
    
    def size(self) -> int:
        """
        Get the number of elements in the stack.
        
        Returns:
            The number of elements in the stack.
            
        Time Complexity:
            O(1)
        """
        return len(self._data)


__all__ = ['_StackImpl']
