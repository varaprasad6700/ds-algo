import pytest

from src.ds.reduce_array_size_to_half import reduce_arr_to_half_min_set


@pytest.mark.parametrize("arr, expected", [
    ([3, 3, 3, 3, 5, 5, 5, 2, 2, 7], 2),
    ([7, 7, 7, 7, 7], 1)
])
def test_reduce_arr_to_half_min_set(arr, expected):
    assert reduce_arr_to_half_min_set(arr) == expected
