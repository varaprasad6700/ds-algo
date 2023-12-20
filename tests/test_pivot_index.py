import pytest

from src.ds.pivot_index import pivot_index


@pytest.mark.parametrize("nums, expected", [
    ([1, 7, 3, 6, 5, 6], 3),
    ([1, 2, 3], -1),
    ([2, 1, -1], 0)
])
def test_pivot_index(nums, expected):
    assert pivot_index(nums) == expected
