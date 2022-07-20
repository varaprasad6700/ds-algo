import pytest

from src.ds.climbing_stairs import climb_stairs


@pytest.mark.parametrize("inp, expected", [
    (10, 89),
    (1, 1),
    (2, 2),
    (3, 3)
])
def test_climb_stairs(inp, expected):
    assert climb_stairs(inp) == expected
