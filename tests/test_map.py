"""
Unit tests for map data structure.
"""

import pytest
from pythonstl import stl_map, KeyNotFoundError


class TestMap:
    """Test cases for map operations."""
    
    def test_empty_map(self):
        """Test that a new map is empty."""
        m = stl_map()
        assert m.empty() is True
        assert m.size() == 0
    
    def test_insert_single_pair(self):
        """Test inserting a single key-value pair."""
        m = stl_map()
        m.insert("key1", 100)
        assert m.empty() is False
        assert m.size() == 1
        assert m.at("key1") == 100
    
    def test_insert_multiple_pairs(self):
        """Test inserting multiple key-value pairs."""
        m = stl_map()
        m.insert("key1", 100)
        m.insert("key2", 200)
        m.insert("key3", 300)
        assert m.size() == 3
        assert m.at("key1") == 100
        assert m.at("key2") == 200
        assert m.at("key3") == 300
    
    def test_insert_update_existing_key(self):
        """Test that inserting with existing key updates the value."""
        m = stl_map()
        m.insert("key1", 100)
        m.insert("key1", 200)
        assert m.size() == 1
        assert m.at("key1") == 200
    
    def test_at_existing_key(self):
        """Test accessing value with existing key."""
        m = stl_map()
        m.insert("apple", 100)
        m.insert("banana", 200)
        assert m.at("apple") == 100
        assert m.at("banana") == 200
    
    def test_at_nonexistent_key_raises_error(self):
        """Test that accessing non-existent key raises error."""
        m = stl_map()
        m.insert("key1", 100)
        with pytest.raises(KeyNotFoundError):
            m.at("key2")
    
    def test_find_existing_key(self):
        """Test finding an existing key."""
        m = stl_map()
        m.insert("key1", 100)
        m.insert("key2", 200)
        assert m.find("key1") is True
        assert m.find("key2") is True
    
    def test_find_nonexistent_key(self):
        """Test finding a non-existent key."""
        m = stl_map()
        m.insert("key1", 100)
        assert m.find("key2") is False
    
    def test_erase_existing_key(self):
        """Test erasing an existing key."""
        m = stl_map()
        m.insert("key1", 100)
        m.insert("key2", 200)
        m.erase("key1")
        assert m.size() == 1
        assert m.find("key1") is False
        assert m.find("key2") is True
    
    def test_erase_nonexistent_key(self):
        """Test that erasing non-existent key does nothing."""
        m = stl_map()
        m.insert("key1", 100)
        m.erase("key2")  # Should not raise error
        assert m.size() == 1
    
    def test_erase_all_pairs(self):
        """Test erasing all key-value pairs."""
        m = stl_map()
        m.insert("key1", 100)
        m.insert("key2", 200)
        m.insert("key3", 300)
        m.erase("key1")
        m.erase("key2")
        m.erase("key3")
        assert m.empty() is True
        assert m.size() == 0
    
    def test_integer_keys(self):
        """Test map with integer keys."""
        m = stl_map()
        m.insert(1, "one")
        m.insert(2, "two")
        m.insert(3, "three")
        assert m.at(1) == "one"
        assert m.at(2) == "two"
        assert m.find(3) is True

    def test_sorted_order(self):
        """Test that map elements are always sorted by key for both backends."""
        for use_rust in [True, False]:
            m = stl_map(use_rust=use_rust)
            m.insert(30, "thirty")
            m.insert(10, "ten")
            m.insert(20, "twenty")
            # Iterating should yield sorted key-value pairs
            assert list(m) == [(10, "ten"), (20, "twenty"), (30, "thirty")]
