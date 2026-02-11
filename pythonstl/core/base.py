"""
Base classes and type definitions for pystl data structures.

This module provides abstract base classes and common interfaces
for all STL-style data structures in the package.
"""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

# Type variable for generic container elements
T = TypeVar('T')
K = TypeVar('K')  # For map keys
V = TypeVar('V')  # For map values


class ContainerBase(ABC, Generic[T]):
    """
    Abstract base class for all STL-style containers.
    
    Provides common interface methods that all containers must implement.
    """
    
    @abstractmethod
    def empty(self) -> bool:
        """
        Check if the container is empty.
        
        Returns:
            bool: True if container is empty, False otherwise.
            
        Time Complexity:
            O(1)
        """
        pass
    
    @abstractmethod
    def size(self) -> int:
        """
        Get the number of elements in the container.
        
        Returns:
            int: Number of elements in the container.
            
        Time Complexity:
            O(1)
        """
        pass


__all__ = ['ContainerBase', 'T', 'K', 'V']
