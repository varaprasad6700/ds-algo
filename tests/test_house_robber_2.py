import pytest

from src.ds.house_robber_2 import rob


@pytest.mark.parametrize("inp, expected", [
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3)
])
def test_rob(inp, expected):
    assert rob(inp) == expected
