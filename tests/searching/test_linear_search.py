import pytest
from src.searching.linear_search import linear_search

def test_linear_search():
    arr = [10, 7, 8, 9, 1, 5]
    assert linear_search(arr, 8) == 2
    assert linear_search(arr, 1) == 4
    assert linear_search(arr, 11) == -1
