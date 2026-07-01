"""
PythonSTL - Python Standard Template Library

A Python package that replicates C++ STL-style data structures
using the Facade Design Pattern.

This package provides clean, STL-compliant interfaces for common
data structures while hiding implementation details from users.
"""

__version__ = "1.1.6"
__author__ = "PySTL Contributors"

from pythonstl.facade.stack import stack
from pythonstl.facade.queue import queue
from pythonstl.facade.vector import vector
from pythonstl.facade.set import stl_set
from pythonstl.facade.map import stl_map
from pythonstl.facade.priority_queue import priority_queue
from pythonstl.facade.algorithms import (
    next_permutation,
    prev_permutation,
    nth_element,
    partition,
    lower_bound,
    upper_bound,
    binary_search,
    equal_range
)

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
    # Algorithms
    'next_permutation',
    'prev_permutation',
    'nth_element',
    'partition',
    'lower_bound',
    'upper_bound',
    'binary_search',
    'equal_range',
    # Exceptions
    'PySTLException',
    'EmptyContainerError',
    'OutOfRangeError',
    'KeyNotFoundError',
    # Metadata
    '__version__',
    '__author__'
]
