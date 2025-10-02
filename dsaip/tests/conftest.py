import pytest
from random import seed

@pytest.fixture
def random():
    seed(42)