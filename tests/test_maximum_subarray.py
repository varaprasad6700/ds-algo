from typing import List

import pytest

from src.ds.maximum_subarray import max_sub_array


@pytest.mark.parametrize("numbers, expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23)
])
def test_maximum_subarray(numbers: List[int], expected: int):
    assert max_sub_array(numbers) == expected
