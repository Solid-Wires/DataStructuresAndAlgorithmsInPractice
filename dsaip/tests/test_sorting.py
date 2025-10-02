import pytest
import pytest_benchmark
import json
from pathlib import Path
from algorithms import bubble_sort, insertion_sort, merge_sort

DATA_PATTERNS = Path(__file__).parent / "data/patterns.json"

def load_int_pattern(idx: int):
    with DATA_PATTERNS.open('r') as file:
        data = json.load(file)
    return data["integer_lists"][idx]

# Base tests

# def test_bubble_sort():
#     pattern = load_int_pattern(0)
#     list = pattern["initial"]
#     bubble_sort(list)
#     print(list, sep=',')
#     assert list == pattern["expected"]

def test_insertion_sort():
    pattern = load_int_pattern(0)
    list = pattern["initial"]
    insertion_sort(list)
    print(list, sep=',')
    assert list == pattern["expected"]

# def test_merge_sort():
#     pattern = load_int_pattern(0)
#     list = pattern["initial"]
#     merge_sort(list)
#     print(list, sep=',')
#     assert list == pattern["expected"]

# Large input tests

def test_insertion_sort_large_n(benchmark):
    pattern = load_int_pattern(1)
    list = pattern["initial"]
    benchmark(insertion_sort, list)
    print(list, sep=',')
    assert list == pattern["expected"]
