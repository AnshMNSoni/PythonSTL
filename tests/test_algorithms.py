import pytest
from pythonstl import next_permutation, prev_permutation, nth_element, partition
from pythonstl.facade.algorithms import RUST_AVAILABLE

# Run tests on both implementations (Rust and pure-Python)
PARAMS = [False]
if RUST_AVAILABLE:
    PARAMS.append(True)

@pytest.mark.parametrize("use_rust", PARAMS)
def test_next_permutation(use_rust):
    # Basic sorted case
    arr = [1, 2, 3]
    has_next = next_permutation(arr, use_rust=use_rust)
    assert has_next is True
    assert arr == [1, 3, 2]
    
    # Boundary/Last permutation case
    arr = [3, 2, 1]
    has_next = next_permutation(arr, use_rust=use_rust)
    assert has_next is False
    assert arr == [1, 2, 3]
    
    # Duplicates case
    arr = [1, 1, 5]
    assert next_permutation(arr, use_rust=use_rust) is True
    assert arr == [1, 5, 1]
    assert next_permutation(arr, use_rust=use_rust) is True
    assert arr == [5, 1, 1]
    assert next_permutation(arr, use_rust=use_rust) is False
    assert arr == [1, 1, 5]

@pytest.mark.parametrize("use_rust", PARAMS)
def test_prev_permutation(use_rust):
    # Basic descending case
    arr = [3, 2, 1]
    has_prev = prev_permutation(arr, use_rust=use_rust)
    assert has_prev is True
    assert arr == [3, 1, 2]
    
    # Boundary/First permutation case
    arr = [1, 2, 3]
    has_prev = prev_permutation(arr, use_rust=use_rust)
    assert has_prev is False
    assert arr == [3, 2, 1]

@pytest.mark.parametrize("use_rust", PARAMS)
def test_nth_element(use_rust):
    # Find median (nth = 4 on 9 elements)
    arr = [9, 7, 5, 1, 2, 3, 6, 4, 8]
    nth = 4
    nth_element(arr, nth, use_rust=use_rust)
    
    val = arr[nth]
    assert val == 5
    for i in range(nth):
        assert arr[i] <= val
    for i in range(nth + 1, len(arr)):
        assert arr[i] >= val
        
    # Single element and simple boundaries
    arr = [2, 1]
    nth_element(arr, 0, use_rust=use_rust)
    assert arr[0] == 1
    assert arr[1] == 2

@pytest.mark.parametrize("use_rust", PARAMS)
def test_partition(use_rust):
    # Partition even numbers to the front
    arr = [1, 2, 3, 4, 5, 6, 7, 8]
    boundary = partition(arr, lambda x: x % 2 == 0, use_rust=use_rust)
    
    assert boundary == 4
    for i in range(boundary):
        assert arr[i] % 2 == 0
    for i in range(boundary, len(arr)):
        assert arr[i] % 2 != 0
