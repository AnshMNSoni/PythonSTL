"""
Unit tests for vector data structure.
"""

import pytest
from pythonstl import vector, EmptyContainerError, OutOfRangeError


class TestVector:
    """Test cases for vector operations."""
    
    def test_empty_vector(self):
        """Test that a new vector is empty."""
        v = vector()
        assert v.empty() is True
        assert v.size() == 0
    
    def test_push_back_single_element(self):
        """Test pushing a single element."""
        v = vector()
        v.push_back(10)
        assert v.empty() is False
        assert v.size() == 1
        assert v.at(0) == 10
    
    def test_push_back_multiple_elements(self):
        """Test pushing multiple elements."""
        v = vector()
        v.push_back(10)
        v.push_back(20)
        v.push_back(30)
        assert v.size() == 3
        assert v.at(0) == 10
        assert v.at(1) == 20
        assert v.at(2) == 30
    
    def test_pop_back(self):
        """Test popping elements."""
        v = vector()
        v.push_back(10)
        v.push_back(20)
        v.pop_back()
        assert v.size() == 1
        assert v.at(0) == 10
    
    def test_pop_back_empty_raises_error(self):
        """Test that popping from empty vector raises error."""
        v = vector()
        with pytest.raises(EmptyContainerError):
            v.pop_back()
    
    def test_at_valid_index(self):
        """Test accessing elements at valid indices."""
        v = vector()
        v.push_back(100)
        v.push_back(200)
        v.push_back(300)
        assert v.at(0) == 100
        assert v.at(1) == 200
        assert v.at(2) == 300
    
    def test_at_invalid_index_raises_error(self):
        """Test that accessing invalid index raises error."""
        v = vector()
        v.push_back(10)
        with pytest.raises(OutOfRangeError):
            v.at(5)
        with pytest.raises(OutOfRangeError):
            v.at(-1)
    
    def test_insert_at_beginning(self):
        """Test inserting at the beginning."""
        v = vector()
        v.push_back(20)
        v.push_back(30)
        v.insert(0, 10)
        assert v.size() == 3
        assert v.at(0) == 10
        assert v.at(1) == 20
        assert v.at(2) == 30
    
    def test_insert_at_middle(self):
        """Test inserting in the middle."""
        v = vector()
        v.push_back(10)
        v.push_back(30)
        v.insert(1, 20)
        assert v.size() == 3
        assert v.at(0) == 10
        assert v.at(1) == 20
        assert v.at(2) == 30
    
    def test_insert_at_end(self):
        """Test inserting at the end."""
        v = vector()
        v.push_back(10)
        v.push_back(20)
        v.insert(2, 30)
        assert v.size() == 3
        assert v.at(2) == 30
    
    def test_insert_invalid_position_raises_error(self):
        """Test that inserting at invalid position raises error."""
        v = vector()
        v.push_back(10)
        with pytest.raises(OutOfRangeError):
            v.insert(5, 20)
    
    def test_erase_at_beginning(self):
        """Test erasing at the beginning."""
        v = vector()
        v.push_back(10)
        v.push_back(20)
        v.push_back(30)
        v.erase(0)
        assert v.size() == 2
        assert v.at(0) == 20
        assert v.at(1) == 30
    
    def test_erase_at_middle(self):
        """Test erasing in the middle."""
        v = vector()
        v.push_back(10)
        v.push_back(20)
        v.push_back(30)
        v.erase(1)
        assert v.size() == 2
        assert v.at(0) == 10
        assert v.at(1) == 30
    
    def test_erase_invalid_position_raises_error(self):
        """Test that erasing at invalid position raises error."""
        v = vector()
        v.push_back(10)
        with pytest.raises(OutOfRangeError):
            v.erase(5)
    
    def test_clear(self):
        """Test clearing the vector."""
        v = vector()
        v.push_back(10)
        v.push_back(20)
        v.push_back(30)
        v.clear()
        assert v.empty() is True
        assert v.size() == 0
    
    def test_capacity(self):
        """Test capacity management."""
        v = vector()
        assert v.capacity() == 0
        v.push_back(10)
        assert v.capacity() > 0
