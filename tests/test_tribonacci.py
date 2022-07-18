import pytest

from src.ds.tribonacci import tribonacci


@pytest.mark.parametrize("inp, expected", [
    (25, 1389537),
    (4, 4),
    (3, 2)
])
def test_tribonacci(inp, expected):
    assert tribonacci(inp) == expected
