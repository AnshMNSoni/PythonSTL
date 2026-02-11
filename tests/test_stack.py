"""
Unit tests for stack data structure.
"""

import pytest
from pythonstl import stack, EmptyContainerError


class TestStack:
    """Test cases for stack operations."""
    
    def test_empty_stack(self):
        """Test that a new stack is empty."""
        s = stack()
        assert s.empty() is True
        assert s.size() == 0
    
    def test_push_single_element(self):
        """Test pushing a single element."""
        s = stack()
        s.push(10)
        assert s.empty() is False
        assert s.size() == 1
        assert s.top() == 10
    
    def test_push_multiple_elements(self):
        """Test pushing multiple elements."""
        s = stack()
        s.push(10)
        s.push(20)
        s.push(30)
        assert s.size() == 3
        assert s.top() == 30
    
    def test_pop_single_element(self):
        """Test popping from a single-element stack."""
        s = stack()
        s.push(10)
        s.pop()
        assert s.empty() is True
        assert s.size() == 0
    
    def test_pop_multiple_elements(self):
        """Test popping multiple elements."""
        s = stack()
        s.push(10)
        s.push(20)
        s.push(30)
        s.pop()
        assert s.top() == 20
        s.pop()
        assert s.top() == 10
        assert s.size() == 1
    
    def test_lifo_order(self):
        """Test that stack follows LIFO order."""
        s = stack()
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            s.push(elem)
        
        for elem in reversed(elements):
            assert s.top() == elem
            s.pop()
    
    def test_top_empty_stack_raises_error(self):
        """Test that accessing top of empty stack raises error."""
        s = stack()
        with pytest.raises(EmptyContainerError):
            s.top()
    
    def test_pop_empty_stack_raises_error(self):
        """Test that popping from empty stack raises error."""
        s = stack()
        with pytest.raises(EmptyContainerError):
            s.pop()
    
    def test_mixed_types(self):
        """Test stack with mixed types."""
        s = stack()
        s.push(10)
        s.push("hello")
        s.push(3.14)
        assert s.top() == 3.14
        s.pop()
        assert s.top() == "hello"
        s.pop()
        assert s.top() == 10
