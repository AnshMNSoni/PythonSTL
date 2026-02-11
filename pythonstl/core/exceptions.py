"""
Custom exceptions for pystl data structures.

This module defines all custom exceptions used throughout the package
to provide clear error messages matching C++ STL behavior.
"""


class PySTLException(Exception):
    """Base exception class for all pystl exceptions."""
    pass


class EmptyContainerError(PySTLException):
    """
    Exception raised when attempting to access elements from an empty container.

    This matches the behavior of C++ STL when accessing empty containers
    (e.g., calling top() on an empty stack).
    """

    def __init__(self, container_type: str):
        self.container_type = container_type
        super().__init__(f"Cannot access element from empty {container_type}")


class OutOfRangeError(PySTLException):
    """
    Exception raised when accessing an invalid index or position.

    This matches C++ STL's std::out_of_range exception.
    """

    def __init__(self, index: int, size: int):
        self.index = index
        self.size = size
        super().__init__(f"Index {index} is out of range for container of size {size}")


class KeyNotFoundError(PySTLException):
    """
    Exception raised when a key is not found in an associative container.

    This matches C++ STL behavior when accessing non-existent keys in maps.
    """

    def __init__(self, key):
        self.key = key
        super().__init__(f"Key '{key}' not found in container")


__all__ = [
    'PySTLException',
    'EmptyContainerError',
    'OutOfRangeError',
    'KeyNotFoundError'
]
