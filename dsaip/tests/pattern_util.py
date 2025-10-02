from pathlib import Path
from json import load as json_load
from random import sample
# Helper definition for retrieval of input patterns for edge cases

# File path for data patterns
DATA_PATTERNS: Path = Path(__file__).parent / "data/patterns.json"

# Helper function which loads integer list patterns for edge cases
def load_int_pattern(idx: int) -> dict:
    with DATA_PATTERNS.open('r') as file:
        data = json_load(file)
    return data["integer_arrays_sorting"][idx]

# Helper function which generates fixed input sizes of random number patterns
def generate_random_input_size_n(size: int) -> dict:
    sample_arr: list[int] = sample(range(20000), size)
    sorted_arr: list[int] = sorted(sample_arr) # Using built-in sort
    return {
        "initial": sample_arr,
        "expected": sorted_arr
    }
