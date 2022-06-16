import pytest

from src.ds.dutch_national_flag import dutch_national_flag


@pytest.mark.parametrize("nums, expected", [
    ([0, 0, 1, 0, 2, 1, 2], [0, 0, 0, 1, 1, 2, 2]),
    ([0], [0]),
    ([], []),
    ([1, 1, 0, 0], [0, 0, 1, 1])
])
def test_dutch_national_flag(nums, expected):
    assert dutch_national_flag(nums) == expected
