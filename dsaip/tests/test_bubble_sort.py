import pytest
from algorithms import bubble_sort
from .benchmark_util import benchmark_run_sort_fn as run_sort_fn
from .pattern_util import generate_random_input_size_n

@pytest.mark.parametrize("n", [20, 200, 2000])
def test_bubble_sort_scaling(benchmark, n: int):
    pattern: dict = generate_random_input_size_n(n)
    result: list[int] = benchmark(lambda: run_sort_fn(bubble_sort, pattern["initial"]))
    assert result == pattern["expected"]
