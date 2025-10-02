# Helper functions which sandbox functions so that benchmark can study run cases


# For all sort functions
def benchmark_run_sort_fn(fn: callable, initial: list[int]) -> list[int]:
    arr = initial.copy() # Otherwise, arr gets already sorted and benchmark is useless
    fn(arr)
    return arr
