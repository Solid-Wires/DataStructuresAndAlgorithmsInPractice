from pathlib import Path
from json import load as json_load
from random import sample
# Helper definitions for retrieval of input patterns for edge cases
# A pattern is a dataset which explains an initial set of inputs and an expected
# output when such inputs are processed through a function.
# Or, to put it simply, edge case inputs.


# File path for data patterns
DATA_PATTERNS: Path = Path(__file__).parent.parent / "data/patterns.json"

# Loads integer list patterns for edge cases
def load_int_arr_sorting_pattern(idx: int) -> dict:
    with DATA_PATTERNS.open('r') as file:
        data = json_load(file)
    return data["integer_arrays_sorting"][idx]

# Generates input size n of random integer patterns for sorting algorithms
def generate_random_int_arr_sorting_input_size(n: int) -> dict:
    sample_arr: list[int] = sample(range(20000), n)
    sorted_arr: list[int] = sorted(sample_arr) # Using built-in sort
    return {
        "initial": sample_arr,
        "expected": sorted_arr,
        "summary": "Randomly generated input of size n"
    }
