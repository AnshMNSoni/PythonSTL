"""
Unit tests for queue data structure.
"""

import pytest
from pythonstl import queue, EmptyContainerError


class TestQueue:
    """Test cases for queue operations."""
    
    def test_empty_queue(self):
        """Test that a new queue is empty."""
        q = queue()
        assert q.empty() is True
        assert q.size() == 0
    
    def test_push_single_element(self):
        """Test pushing a single element."""
        q = queue()
        q.push(10)
        assert q.empty() is False
        assert q.size() == 1
        assert q.front() == 10
        assert q.back() == 10
    
    def test_push_multiple_elements(self):
        """Test pushing multiple elements."""
        q = queue()
        q.push(10)
        q.push(20)
        q.push(30)
        assert q.size() == 3
        assert q.front() == 10
        assert q.back() == 30
    
    def test_pop_single_element(self):
        """Test popping from a single-element queue."""
        q = queue()
        q.push(10)
        q.pop()
        assert q.empty() is True
        assert q.size() == 0
    
    def test_pop_multiple_elements(self):
        """Test popping multiple elements."""
        q = queue()
        q.push(10)
        q.push(20)
        q.push(30)
        q.pop()
        assert q.front() == 20
        q.pop()
        assert q.front() == 30
        assert q.size() == 1
    
    def test_fifo_order(self):
        """Test that queue follows FIFO order."""
        q = queue()
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            q.push(elem)
        
        for elem in elements:
            assert q.front() == elem
            q.pop()
    
    def test_front_empty_queue_raises_error(self):
        """Test that accessing front of empty queue raises error."""
        q = queue()
        with pytest.raises(EmptyContainerError):
            q.front()
    
    def test_back_empty_queue_raises_error(self):
        """Test that accessing back of empty queue raises error."""
        q = queue()
        with pytest.raises(EmptyContainerError):
            q.back()
    
    def test_pop_empty_queue_raises_error(self):
        """Test that popping from empty queue raises error."""
        q = queue()
        with pytest.raises(EmptyContainerError):
            q.pop()
    
    def test_mixed_types(self):
        """Test queue with mixed types."""
        q = queue()
        q.push(10)
        q.push("hello")
        q.push(3.14)
        assert q.front() == 10
        assert q.back() == 3.14
        q.pop()
        assert q.front() == "hello"
