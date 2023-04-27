import pytest
from src.sorting.quick_sort import quick_sort

def test_quick_sort():
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr)
    assert arr == [1, 5, 7, 8, 9, 10]
