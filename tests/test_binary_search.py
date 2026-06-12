import pytest
from pythonstl import lower_bound, upper_bound, binary_search, equal_range

# Create a custom class to test custom comparator
class Item:
    def __init__(self, val):
        self.val = val
    def __repr__(self):
        return f"Item({self.val})"


def test_lower_bound_std():
    for use_rust in [True, False]:
        arr = [1, 2, 2, 2, 3, 5, 8]
        # Element present
        assert lower_bound(arr, 2, use_rust=use_rust) == 1
        assert lower_bound(arr, 3, use_rust=use_rust) == 4
        # Element not present, fits in middle
        assert lower_bound(arr, 4, use_rust=use_rust) == 5
        # Element smaller than all
        assert lower_bound(arr, 0, use_rust=use_rust) == 0
        # Element larger than all
        assert lower_bound(arr, 10, use_rust=use_rust) == len(arr)


def test_upper_bound_std():
    for use_rust in [True, False]:
        arr = [1, 2, 2, 2, 3, 5, 8]
        # Element present
        assert upper_bound(arr, 2, use_rust=use_rust) == 4
        assert upper_bound(arr, 3, use_rust=use_rust) == 5
        # Element not present, fits in middle
        assert upper_bound(arr, 4, use_rust=use_rust) == 5
        # Element smaller than all
        assert upper_bound(arr, 0, use_rust=use_rust) == 0
        # Element larger than all
        assert upper_bound(arr, 10, use_rust=use_rust) == len(arr)


def test_binary_search_std():
    for use_rust in [True, False]:
        arr = [1, 2, 2, 2, 3, 5, 8]
        # Element present
        assert binary_search(arr, 2, use_rust=use_rust) is True
        assert binary_search(arr, 3, use_rust=use_rust) is True
        assert binary_search(arr, 5, use_rust=use_rust) is True
        # Element not present
        assert binary_search(arr, 4, use_rust=use_rust) is False
        assert binary_search(arr, 0, use_rust=use_rust) is False
        assert binary_search(arr, 10, use_rust=use_rust) is False


def test_equal_range_std():
    for use_rust in [True, False]:
        arr = [1, 2, 2, 2, 3, 5, 8]
        assert equal_range(arr, 2, use_rust=use_rust) == (1, 4)
        assert equal_range(arr, 3, use_rust=use_rust) == (4, 5)
        assert equal_range(arr, 4, use_rust=use_rust) == (5, 5)
        assert equal_range(arr, 0, use_rust=use_rust) == (0, 0)
        assert equal_range(arr, 10, use_rust=use_rust) == (len(arr), len(arr))


def test_empty_and_single():
    for use_rust in [True, False]:
        # Empty list
        arr = []
        assert lower_bound(arr, 5, use_rust=use_rust) == 0
        assert upper_bound(arr, 5, use_rust=use_rust) == 0
        assert binary_search(arr, 5, use_rust=use_rust) is False
        assert equal_range(arr, 5, use_rust=use_rust) == (0, 0)
        
        # Single element
        arr = [5]
        assert lower_bound(arr, 3, use_rust=use_rust) == 0
        assert lower_bound(arr, 5, use_rust=use_rust) == 0
        assert lower_bound(arr, 7, use_rust=use_rust) == 1
        
        assert upper_bound(arr, 3, use_rust=use_rust) == 0
        assert upper_bound(arr, 5, use_rust=use_rust) == 1
        assert upper_bound(arr, 7, use_rust=use_rust) == 1
        
        assert binary_search(arr, 5, use_rust=use_rust) is True
        assert binary_search(arr, 3, use_rust=use_rust) is False
        assert equal_range(arr, 5, use_rust=use_rust) == (0, 1)


def test_custom_comparator():
    # Comparator returns True if element < val
    def item_comp(item1, item2):
        return item1.val < item2.val

    for use_rust in [True, False]:
        arr = [Item(1), Item(2), Item(2), Item(3)]
        val = Item(2)
        
        assert lower_bound(arr, val, comp=item_comp, use_rust=use_rust) == 1
        assert upper_bound(arr, val, comp=item_comp, use_rust=use_rust) == 3
        assert binary_search(arr, val, comp=item_comp, use_rust=use_rust) is True
        assert equal_range(arr, val, comp=item_comp, use_rust=use_rust) == (1, 3)
        
        # Element not present
        val_not = Item(4)
        assert lower_bound(arr, val_not, comp=item_comp, use_rust=use_rust) == 4
        assert binary_search(arr, val_not, comp=item_comp, use_rust=use_rust) is False
