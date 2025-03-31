# Using pytest
import pytest
from mymodule import multiply

def test_multiply():
    """This is a multiplication"""
    assert multiply(2, 3) == 6
    assert multiply(-1, 5) == -5
