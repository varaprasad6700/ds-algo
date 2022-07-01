import pytest

from src.ds.two_sum import two_sum


@pytest.mark.parametrize("inp, target, expected", [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2])
])
def test_two_sum(inp, target, expected):
    assert two_sum(inp, target) == expected
