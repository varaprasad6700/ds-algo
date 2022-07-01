import pytest

from src.ds.move_zeros import move_zeros


@pytest.mark.parametrize("inp, expected", [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
    ([0], [0])
])
def test_move_zeros(inp, expected):
    assert move_zeros(inp) == expected
