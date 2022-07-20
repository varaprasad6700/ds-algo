import pytest

from src.ds.min_cost_climbing_stairs import min_cost_climbing_stairs


@pytest.mark.parametrize("inp, expected", [
    ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ([10, 15, 20], 15)
])
def test_min_cost_climbing_stairs(inp, expected):
    assert min_cost_climbing_stairs(inp) == expected
