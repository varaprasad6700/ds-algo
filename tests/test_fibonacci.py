import pytest

from src.ds.fibonacci import fib, fib_td


@pytest.mark.parametrize("inp, expected", [
    (10, 55),
    (0, 0),
    (1, 1),
    (4, 3)
])
def test_fib(inp, expected):
    assert fib(inp) == expected
    assert fib_td(inp) == expected
