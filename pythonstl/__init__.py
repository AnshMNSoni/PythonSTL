"""
PythonSTL - Python Standard Template Library

A Python package that replicates C++ STL-style data structures
using the Facade Design Pattern.

This package provides clean, STL-compliant interfaces for common
data structures while hiding implementation details from users.
"""

__version__ = "1.1.10"
__author__ = "PySTL Contributors"

from pythonstl.containers.stack import stack
from pythonstl.containers.queue import queue
from pythonstl.containers.vector import vector
from pythonstl.containers.set import stl_set
from pythonstl.containers.map import stl_map
from pythonstl.containers.priority_queue import priority_queue
from pythonstl.containers.algorithms import (
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
from pythonstl.utility.exceptions import (
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
