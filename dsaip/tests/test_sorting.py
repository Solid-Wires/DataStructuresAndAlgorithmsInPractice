import pytest
import pytest_benchmark
import json
import random
from pathlib import Path
from algorithms import bubble_sort, insertion_sort, merge_sort

DATA_PATTERNS = Path(__file__).parent / "data/patterns.json"

def load_int_pattern(idx: int) -> dict:
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

# Medium input tests
MED_INPUT_PATTERN_IDX = 3

@pytest.mark.skip(reason="Sample size not large enough to be interesting")
def test_bubble_sort_large_n(benchmark):
    pattern = load_int_pattern(MED_INPUT_PATTERN_IDX)
    arr = pattern["initial"]
    benchmark(bubble_sort, arr)
    assert arr == pattern["expected"]

@pytest.mark.skip(reason="Sample size not large enough to be interesting")
def test_insertion_sort_large_n(benchmark):
    pattern = load_int_pattern(MED_INPUT_PATTERN_IDX)
    arr = pattern["initial"]
    benchmark(insertion_sort, arr)
    assert arr == pattern["expected"]

@pytest.mark.skip(reason="Sample size not large enough to be interesting")
def test_merge_sort_large_n(benchmark):
    pattern = load_int_pattern(MED_INPUT_PATTERN_IDX)
    arr = pattern["initial"]
    benchmark(merge_sort, arr)
    assert arr == pattern["expected"]

# Huge, random input benchmarking tests
def generate_random_input_size(size: int) -> dict:
    sample_arr = random.sample(range(10000), size)
    sorted_arr = sample_arr.copy()
    sorted_arr.sort() # Using built-in sort
    return {
        "initial": sample_arr,
        "expected": sorted_arr
    }

def test_bubble_sort_random_huge_n(benchmark):
    pattern = generate_random_input_size(2000)
    arr = pattern["initial"]
    benchmark(bubble_sort, arr)
    assert arr == pattern["expected"]

def test_insertion_sort_random_huge_n(benchmark):
    pattern = generate_random_input_size(2000)
    arr = pattern["initial"]
    benchmark(insertion_sort, arr)
    assert arr == pattern["expected"]

def test_merge_sort_random_huge_n(benchmark):
    pattern = generate_random_input_size(2000)
    arr = pattern["initial"]
    benchmark(merge_sort, arr)
    assert arr == pattern["expected"]
