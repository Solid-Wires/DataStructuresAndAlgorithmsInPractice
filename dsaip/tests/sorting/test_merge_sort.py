import pytest
from algorithms import merge_sort
from tests.util import benchmark_run_sort_fn as run_sort_fn
from tests.util import generate_random_int_arr_sorting_input_size as generate_random_input_size
from tests.util import load_int_arr_sorting_pattern as load_pattern

# Scaling + Functionality

@pytest.mark.parametrize("n", [20, 200, 2000])
def test_merge_sort_scaling(benchmark, n: int):
    pattern: dict = generate_random_input_size(n)
    result: list[int] = benchmark(lambda: run_sort_fn(merge_sort, pattern["initial"]))
    assert result == pattern["expected"]

# Edge case patterns

def test_merge_sort_negative_integers():
    pattern: dict = load_pattern(3)
    result: list[int] = run_sort_fn(merge_sort, pattern["initial"])
    assert result == pattern["expected"]

def test_merge_sort_contains_zero():
    pattern: dict = load_pattern(4)
    result: list[int] = run_sort_fn(merge_sort, pattern["initial"])
    assert result == pattern["expected"]

def test_merge_sort_duplicate_values():
    pattern: dict = load_pattern(5)
    result: list[int] = run_sort_fn(merge_sort, pattern["initial"])
    assert result == pattern["expected"]
