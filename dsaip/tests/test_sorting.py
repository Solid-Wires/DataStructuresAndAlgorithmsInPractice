import pytest
import pytest_benchmark
import json
from pathlib import Path
from algorithms import bubble_sort, insertion_sort, merge_sort

DATA_PATTERNS = Path(__file__).parent / "data/patterns.json"

def load_int_pattern(idx: int):
    with DATA_PATTERNS.open('r') as file:
        data = json.load(file)
    return data["integer_arrays"][idx]

# Base tests

def test_bubble_sort():
    pattern = load_int_pattern(1)
    arr = pattern["initial"]
    bubble_sort(arr)
    print(arr, sep=',')
    assert arr == pattern["expected"]

def test_insertion_sort():
    pattern = load_int_pattern(0)
    arr = pattern["initial"]
    insertion_sort(arr)
    print(arr, sep=',')
    assert arr == pattern["expected"]

def test_merge_sort():
    pattern = load_int_pattern(2)
    arr = pattern["initial"]
    merge_sort(arr)
    print(arr, sep=',')
    assert arr == pattern["expected"]

# Large input tests
LARGE_INPUT_PATTERN_IDX = 3

def test_bubble_sort_large_n(benchmark):
    pattern = load_int_pattern(LARGE_INPUT_PATTERN_IDX)
    arr = pattern["initial"]
    benchmark(bubble_sort, arr)
    print(arr, sep=',')
    assert arr == pattern["expected"]

def test_insertion_sort_large_n(benchmark):
    pattern = load_int_pattern(LARGE_INPUT_PATTERN_IDX)
    arr = pattern["initial"]
    benchmark(insertion_sort, arr)
    print(arr, sep=',')
    assert arr == pattern["expected"]

def test_merge_sort_large_n(benchmark):
    pattern = load_int_pattern(LARGE_INPUT_PATTERN_IDX)
    arr = pattern["initial"]
    benchmark(merge_sort, arr)
    print(arr, sep=',')
    assert arr == pattern["expected"]
