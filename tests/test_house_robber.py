import pytest

from src.ds.house_robber import rob, rob_optim


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 3, 1], 4),
    ([2, 1], 2),
    ([2, 7, 9, 3, 1], 12)
])
def test_rob(inp, expected):
    assert rob(inp) == expected
    assert rob_optim(inp) == expected
