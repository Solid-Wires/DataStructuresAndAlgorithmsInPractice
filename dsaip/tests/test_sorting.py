import pytest
import pytest_benchmark
from algorithms import bubble_sort, insertion_sort, merge_sort
from .pattern_util import generate_random_input_size_n

# Helper function which sandboxes sort functions so that benchmark can study run cases
def benchmark_run_sort_fn(fn: callable, initial: list[int]) -> list[int]:
    arr = initial.copy() # Otherwise, arr gets already sorted and benchmark is useless
    fn(arr)
    return arr
    
@pytest.mark.parametrize("n", [20, 200, 2000])
def test_bubble_sort_scaling(benchmark, n: int):
    pattern: dict = generate_random_input_size_n(n)
    result: list[int] = benchmark(lambda: benchmark_run_sort_fn(bubble_sort, pattern["initial"]))
    assert result == pattern["expected"]

@pytest.mark.parametrize("n", [20, 200, 2000])
def test_insertion_sort_scaling(benchmark, n: int):
    pattern: dict = generate_random_input_size_n(n)
    result: list[int] = benchmark(lambda: benchmark_run_sort_fn(insertion_sort, pattern["initial"]))
    assert result == pattern["expected"]

@pytest.mark.parametrize("n", [20, 200, 2000])
def test_merge_sort_scaling(benchmark, n: int):
    pattern: dict = generate_random_input_size_n(n)
    result: list[int] = benchmark(lambda: benchmark_run_sort_fn(merge_sort, pattern["initial"]))
    assert result == pattern["expected"]
