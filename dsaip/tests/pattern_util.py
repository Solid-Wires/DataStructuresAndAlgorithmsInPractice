from pathlib import Path
from json import load as json_load
from random import sample
# Helper definitions for retrieval of input patterns for edge cases


# File path for data patterns
DATA_PATTERNS: Path = Path(__file__).parent / "data/patterns.json"

# Loads integer list patterns for edge cases
def load_int_arr_sorting_pattern(idx: int) -> dict:
    with DATA_PATTERNS.open('r') as file:
        data = json_load(file)
    return data["integer_arrays_sorting"][idx]

# Generates fixed input sizes of random number patterns
def generate_random_int_arr_sorting_input_size(n: int) -> dict:
    sample_arr: list[int] = sample(range(20000), n)
    sorted_arr: list[int] = sorted(sample_arr) # Using built-in sort
    return {
        "initial": sample_arr,
        "expected": sorted_arr,
        "summary": "Randomly generated input of size n"
    }
