from typing import List

import pytest

from src.ds.maximum_subarray import max_sub_array, max_sub_array_with_start_and_end


@pytest.mark.parametrize("numbers, expected", [
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], [6, 3, 6]),
    ([1], [1, 0, 0]),
    ([5, 4, -1, 7, 8], [23, 0, 4]),
    ([5, 4, -10, 7, 8], [15, 3, 4])
])
def test_maximum_subarray(numbers: List[int], expected: List[int]):
    assert max_sub_array(numbers) == expected[0]
    assert max_sub_array_with_start_and_end(numbers) == expected
