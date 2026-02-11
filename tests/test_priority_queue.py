"""
Unit tests for priority queue data structure.
"""

import pytest
from pythonstl import priority_queue, EmptyContainerError


class TestPriorityQueue:
    """Test cases for priority queue operations."""
    
    def test_empty_priority_queue(self):
        """Test that a new priority queue is empty."""
        pq = priority_queue()
        assert pq.empty() is True
        assert pq.size() == 0
    
    def test_push_single_element(self):
        """Test pushing a single element."""
        pq = priority_queue()
        pq.push(10)
        assert pq.empty() is False
        assert pq.size() == 1
        assert pq.top() == 10
    
    def test_max_heap_order(self):
        """Test that max-heap returns largest element."""
        pq = priority_queue()
        pq.push(30)
        pq.push(10)
        pq.push(50)
        pq.push(20)
        assert pq.top() == 50
    
    def test_max_heap_pop_order(self):
        """Test that elements are popped in descending order."""
        pq = priority_queue()
        elements = [30, 10, 50, 20, 40]
        for elem in elements:
            pq.push(elem)
        
        expected_order = [50, 40, 30, 20, 10]
        for expected in expected_order:
            assert pq.top() == expected
            pq.pop()
    
    def test_min_heap_order(self):
        """Test that min-heap returns smallest element."""
        pq = priority_queue(max_heap=False)
        pq.push(30)
        pq.push(10)
        pq.push(50)
        pq.push(20)
        assert pq.top() == 10
    
    def test_min_heap_pop_order(self):
        """Test that elements are popped in ascending order from min-heap."""
        pq = priority_queue(max_heap=False)
        elements = [30, 10, 50, 20, 40]
        for elem in elements:
            pq.push(elem)
        
        expected_order = [10, 20, 30, 40, 50]
        for expected in expected_order:
            assert pq.top() == expected
            pq.pop()
    
    def test_pop_single_element(self):
        """Test popping from a single-element priority queue."""
        pq = priority_queue()
        pq.push(10)
        pq.pop()
        assert pq.empty() is True
        assert pq.size() == 0
    
    def test_top_empty_raises_error(self):
        """Test that accessing top of empty priority queue raises error."""
        pq = priority_queue()
        with pytest.raises(EmptyContainerError):
            pq.top()
    
    def test_pop_empty_raises_error(self):
        """Test that popping from empty priority queue raises error."""
        pq = priority_queue()
        with pytest.raises(EmptyContainerError):
            pq.pop()
    
    def test_size_after_operations(self):
        """Test size tracking after various operations."""
        pq = priority_queue()
        assert pq.size() == 0
        pq.push(10)
        assert pq.size() == 1
        pq.push(20)
        pq.push(30)
        assert pq.size() == 3
        pq.pop()
        assert pq.size() == 2
        pq.pop()
        pq.pop()
        assert pq.size() == 0
