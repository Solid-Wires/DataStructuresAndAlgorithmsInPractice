import pytest
from random import seed

@pytest.fixture(scope="session", autouse=True)
def set_random_seed():
    seed(42)