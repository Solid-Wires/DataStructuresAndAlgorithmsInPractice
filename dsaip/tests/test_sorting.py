import pytest
import pytest_benchmark
from json import load as json_load
from random import sample
from pathlib import Path
from algorithms import bubble_sort, insertion_sort, merge_sort

# File path for data patterns
DATA_PATTERNS = Path(__file__).parent / "data/patterns.json"

# Helper function which loads integer list patterns for edge cases
def load_int_pattern(idx: int) -> dict:
    with DATA_PATTERNS.open('r') as file:
        data = json_load(file)
    return data["integer_arrays"][idx]

# Helper function which generates fixed input sizes of random numbers
def generate_random_input_size_n(size: int) -> dict:
    sample_arr = sample(range(20000), size)
    sorted_arr = sorted(sample_arr) # Using built-in sort
    return {
        "initial": sample_arr,
        "expected": sorted_arr
    }

# Helper function which sandboxes sort functions so that benchmark can study run cases
def benchmark_run_sort_fn(fn: callable, initial: list[int]):
    arr = initial.copy() # Otherwise, arr gets already sorted and benchmark is useless
    fn(arr)
    return arr
    
@pytest.mark.parametrize("n", [20, 200, 2000])
def test_bubble_sort_scaling(benchmark, n: int):
    pattern = generate_random_input_size_n(n)
    result = benchmark(lambda: benchmark_run_sort_fn(bubble_sort, pattern["initial"]))
    assert result == pattern["expected"]

@pytest.mark.parametrize("n", [20, 200, 2000])
def test_insertion_sort_scaling(benchmark, n: int):
    pattern = generate_random_input_size_n(n)
    result = benchmark(lambda: benchmark_run_sort_fn(insertion_sort, pattern["initial"]))
    assert result == pattern["expected"]

@pytest.mark.parametrize("n", [20, 200, 2000])
def test_merge_sort_scaling(benchmark, n: int):
    pattern = generate_random_input_size_n(n)
    result = benchmark(lambda: benchmark_run_sort_fn(merge_sort, pattern["initial"]))
    assert result == pattern["expected"]
