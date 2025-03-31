import pytest
from math_utils import multiply

@pytest.mark.parametrize("a, b, expected",[
    (2,3,6),
    (0,100,0),
    (-1,5,-5),
    (3,3,9)
])
def test_multiply(a,b,expected):
    assert multiply(a,b) == expected

#with one argument only
@pytest.mark.parametrize("value", [0, 1, 100])
def test_is_positive(value):
    assert value >= 0

#with ids
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 1, 2), (0, 0, 0), (-1, -1, -2)],
    ids=["positive", "zero", "negative"]
)
def test_add(a, b, expected):
    assert a + b == expected