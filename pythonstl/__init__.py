"""
PythonSTL - Python Standard Template Library

A Python package that replicates C++ STL-style data structures
using the Facade Design Pattern.

This package provides clean, STL-compliant interfaces for common
data structures while hiding implementation details from users.
"""

__version__ = "0.1.1"
__author__ = "PySTL Contributors"

from pythonstl.facade.stack import stack
from pythonstl.facade.queue import queue
from pythonstl.facade.vector import vector
from pythonstl.facade.set import stl_set
from pythonstl.facade.map import stl_map
from pythonstl.facade.priority_queue import priority_queue

# Also export exceptions for user error handling
from pythonstl.core.exceptions import (
    PySTLException,
    EmptyContainerError,
    OutOfRangeError,
    KeyNotFoundError
)

__all__ = [
    # Data structures
    'stack',
    'queue',
    'vector',
    'stl_set',
    'stl_map',
    'priority_queue',
    # Exceptions
    'PySTLException',
    'EmptyContainerError',
    'OutOfRangeError',
    'KeyNotFoundError',
    # Metadata
    '__version__',
    '__author__'
]
