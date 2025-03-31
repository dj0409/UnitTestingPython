# test_calculator.py

import pytest
from calculator import add, subtract, multiply, divide, is_even

# Tests for basic arithmetic operations are marked with "math"
@pytest.mark.math
def test_add():
    assert add(3, 2) == 5
    assert add(-1, 1) == 0

@pytest.mark.math
def test_subtract():
    assert subtract(10, 5) == 5
    assert subtract(0, 5) == -5

@pytest.mark.math
def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(-2, 3) == -6

@pytest.mark.math
def test_is_even():
    assert is_even(4) == True
    assert is_even(5) == False
    assert is_even(0) == True

# Tests for division and edge cases are marked with "edge"
@pytest.mark.edge
def test_divide_normal():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

@pytest.mark.edge
def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


# Run only math tests: pytest -m math
# Run only edge tests: pytest -m edge