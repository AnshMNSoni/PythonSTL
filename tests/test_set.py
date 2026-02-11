"""
Unit tests for set data structure.
"""

import pytest
from pythonstl import stl_set


class TestSet:
    """Test cases for set operations."""
    
    def test_empty_set(self):
        """Test that a new set is empty."""
        s = stl_set()
        assert s.empty() is True
        assert s.size() == 0
    
    def test_insert_single_element(self):
        """Test inserting a single element."""
        s = stl_set()
        s.insert(10)
        assert s.empty() is False
        assert s.size() == 1
        assert s.find(10) is True
    
    def test_insert_multiple_elements(self):
        """Test inserting multiple elements."""
        s = stl_set()
        s.insert(10)
        s.insert(20)
        s.insert(30)
        assert s.size() == 3
        assert s.find(10) is True
        assert s.find(20) is True
        assert s.find(30) is True
    
    def test_insert_duplicate_elements(self):
        """Test that duplicate elements are not added."""
        s = stl_set()
        s.insert(10)
        s.insert(10)
        s.insert(10)
        assert s.size() == 1
    
    def test_find_existing_element(self):
        """Test finding an existing element."""
        s = stl_set()
        s.insert(10)
        s.insert(20)
        assert s.find(10) is True
        assert s.find(20) is True
    
    def test_find_nonexistent_element(self):
        """Test finding a non-existent element."""
        s = stl_set()
        s.insert(10)
        assert s.find(20) is False
    
    def test_erase_existing_element(self):
        """Test erasing an existing element."""
        s = stl_set()
        s.insert(10)
        s.insert(20)
        s.erase(10)
        assert s.size() == 1
        assert s.find(10) is False
        assert s.find(20) is True
    
    def test_erase_nonexistent_element(self):
        """Test that erasing non-existent element does nothing."""
        s = stl_set()
        s.insert(10)
        s.erase(20)  # Should not raise error
        assert s.size() == 1
    
    def test_erase_all_elements(self):
        """Test erasing all elements."""
        s = stl_set()
        s.insert(10)
        s.insert(20)
        s.insert(30)
        s.erase(10)
        s.erase(20)
        s.erase(30)
        assert s.empty() is True
        assert s.size() == 0
    
    def test_mixed_types(self):
        """Test set with string elements."""
        s = stl_set()
        s.insert("apple")
        s.insert("banana")
        s.insert("cherry")
        assert s.size() == 3
        assert s.find("banana") is True
        s.erase("banana")
        assert s.find("banana") is False
