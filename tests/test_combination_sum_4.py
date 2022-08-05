import pytest

from src.ds.combination_sum_4 import combination_sum_4


@pytest.mark.parametrize("nums, target, expected", [
    ([1, 2, 3], 4, 7),
    ([9], 3, 0)
])
def test_combination_sum_4(nums, target, expected):
    assert combination_sum_4(nums, target) == expected
