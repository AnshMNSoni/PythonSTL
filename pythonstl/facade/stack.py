"""
Stack facade class.

This module provides the public-facing stack class that users interact with.
"""

from typing import TypeVar
from copy import deepcopy
from pythonstl.implementations.linear._stack_impl import _StackImpl

T = TypeVar('T')


class stack:
    """
    A stack data structure following C++ STL semantics.
    
    This is a LIFO (Last-In-First-Out) container adapter.
    
    Example:
        >>> from pythonstl import stack
        >>> s = stack()
        >>> s.push(10)
        >>> s.push(20)
        >>> s.top()
        20
        >>> len(s)
        2
        >>> bool(s)
        True
    """
    
    def __init__(self) -> None:
        """
        Initialize an empty stack.
        
        Time Complexity:
            O(1)
        """
        self._impl = _StackImpl()
    
    def push(self, value: T) -> None:
        """
        Push an element onto the stack.
        
        Args:
            value: The element to push onto the stack.
            
        Time Complexity:
            O(1) amortized
        """
        self._impl.push(value)
    
    def pop(self) -> None:
        """
        Remove the top element from the stack.
        
        Raises:
            EmptyContainerError: If the stack is empty.
            
        Time Complexity:
            O(1)
        """
        self._impl.pop()
    
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
        return self._impl.top()
    
    def empty(self) -> bool:
        """
        Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
            
        Time Complexity:
            O(1)
        """
        return self._impl.empty()
    
    def size(self) -> int:
        """
        Get the number of elements in the stack.
        
        Returns:
            The number of elements in the stack.
            
        Time Complexity:
            O(1)
        """
        return self._impl.size()
    
    def copy(self) -> 'stack':
        """
        Create a deep copy of the stack.
        
        Returns:
            A new stack with copied elements.
            
        Time Complexity:
            O(n) where n is the number of elements
        """
        new_stack = stack()
        # Copy internal data
        new_stack._impl._data = self._impl._data.copy()
        return new_stack
    
    # Python magic methods
    
    def __len__(self) -> int:
        """
        Get the number of elements (Python len() support).
        
        Returns:
            The number of elements in the stack.
        """
        return self.size()
    
    def __bool__(self) -> bool:
        """
        Check if stack is non-empty (Python bool() support).
        
        Returns:
            True if stack is non-empty, False otherwise.
        """
        return not self.empty()
    
    def __repr__(self) -> str:
        """
        Get string representation of the stack.
        
        Returns:
            String representation showing stack contents.
        """
        elements = [str(elem) for elem in self._impl._data]
        return f"stack([{', '.join(elements)}])"
    
    def __eq__(self, other: object) -> bool:
        """
        Check equality with another stack.
        
        Args:
            other: Another stack to compare with.
            
        Returns:
            True if stacks are equal, False otherwise.
        """
        if not isinstance(other, stack):
            return False
        return self._impl._data == other._impl._data
    
    def __copy__(self) -> 'stack':
        """
        Support for copy.copy().
        
        Returns:
            A shallow copy of the stack.
        """
        return self.copy()
    
    def __deepcopy__(self, memo) -> 'stack':
        """
        Support for copy.deepcopy().
        
        Args:
            memo: Memoization dictionary for deepcopy.
            
        Returns:
            A deep copy of the stack.
        """
        new_stack = stack()
        new_stack._impl._data = deepcopy(self._impl._data, memo)
        return new_stack


__all__ = ['stack']
