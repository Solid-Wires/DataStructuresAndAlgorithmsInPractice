import pytest
import pytest_benchmark
from algorithms import bubble_sort, insertion_sort, merge_sort

def test_base_bubble_sort(benchmark):
    arr = [12, 11, 13, 5, 6]
    expected = [5, 6, 11, 12, 13]
    benchmark(bubble_sort, arr)
    assert arr == expected

def test_base_insertion_sort(benchmark):
    arr = [12, 11, 13, 5, 6]
    expected = [5, 6, 11, 12, 13]
    benchmark(insertion_sort, arr)
    assert arr == expected

def test_base_merge_sort(benchmark):
    arr = [12, 11, 13, 5, 6]
    expected = [5, 6, 11, 12, 13]
    benchmark(merge_sort, arr)
    assert arr == expected
