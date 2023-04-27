import pytest
from src.searching.binary_search import binary_search

def test_binary_search():
    arr = [1, 3, 5, 7, 9, 11, 13, 15]
    assert binary_search(arr, 7) == 3
    assert binary_search(arr, 1) == 0
    assert binary_search(arr, 15) == 7
    assert binary_search(arr, 10) == -1
