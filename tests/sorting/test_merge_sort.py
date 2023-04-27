import pytest
from src.sorting.merge_sort import merge_sort

def test_merge_sort():
    arr = [12, 11, 13, 5, 6, 7]
    assert merge_sort(arr) == [5, 6, 7, 11, 12, 13]

    arr = [64, 34, 25, 12, 22, 11, 90]
    assert merge_sort(arr) == [11, 12, 22, 25, 34, 64, 90]

    arr = [38, 27, 43, 3, 9, 82, 10]
    assert merge_sort(arr) == [3, 9, 10, 27, 38, 43, 82]
