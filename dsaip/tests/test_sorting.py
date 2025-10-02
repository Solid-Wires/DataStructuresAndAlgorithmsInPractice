import pytest
import pytest_benchmark
import json
import random
from pathlib import Path
from algorithms import bubble_sort, insertion_sort, merge_sort

DATA_PATTERNS = Path(__file__).parent / "data/patterns.json"
BENCHMARK_INPUT_SIZE: int = 2000

# Helper function which loads integer list patterns for edge cases
def load_int_pattern(idx: int) -> dict:
    with DATA_PATTERNS.open('r') as file:
        data = json.load(file)
    return data["integer_arrays"][idx]

# Helper function which generates fixed input sizes of random numbers
def generate_random_input_size_n(size: int) -> dict:
    sample_arr = random.sample(range(BENCHMARK_INPUT_SIZE * 100), size)
    sorted_arr = sample_arr.copy()
    sorted_arr.sort() # Using built-in sort
    return {
        "initial": sample_arr,
        "expected": sorted_arr
    }

# Helper function which sandboxes sort functions so that benchmark can study run cases
def benchmark_run_sort_fn(fn: callable, initial: list[int]):
    arr = initial.copy() # Otherwise, arr gets already sorted and benchmark is useless
    fn(arr)
    return arr
    
#@pytest.mark.skip(reason="Sample size was way too large to compute")
def test_bubble_sort_random_ints_constant_n(benchmark):
    pattern = generate_random_input_size_n(BENCHMARK_INPUT_SIZE)
    result = benchmark(lambda: benchmark_run_sort_fn(bubble_sort, pattern["initial"]))
    assert result == pattern["expected"]

def test_insertion_sort_random_ints_constant_n(benchmark):
    pattern = generate_random_input_size_n(BENCHMARK_INPUT_SIZE)
    result = benchmark(lambda: benchmark_run_sort_fn(insertion_sort, pattern["initial"]))
    assert result == pattern["expected"]

def test_merge_sort_random_ints_constant_n(benchmark):
    pattern = generate_random_input_size_n(BENCHMARK_INPUT_SIZE)
    result = benchmark(lambda: benchmark_run_sort_fn(merge_sort, pattern["initial"]))
    assert result == pattern["expected"]
