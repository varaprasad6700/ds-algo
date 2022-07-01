import pytest

from src.ds.rotate_array import rotate_array, rotate_array_optimized


@pytest.mark.parametrize("inp, k, expected", [
    ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
    ([-1, -100, 3, 99], 2, [3, 99, -1, -100])
])
def test_rotate_array(inp, k, expected):
    temp = inp[:]
    rotate_array(temp, k)
    assert temp == expected
    temp = inp[:]
    rotate_array_optimized(temp, k)
    assert temp == expected
