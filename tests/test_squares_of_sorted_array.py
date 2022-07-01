from typing import List

import pytest

from src.ds.squares_of_sorted_array import squares_of_sorted_array


@pytest.mark.parametrize("inp, expected", [
    ([-4, -1, 0, 3, 10], [0, 1, 9, 16, 100]),
    ([-7, -3, 2, 3, 11], [4, 9, 9, 49, 121])
])
def test_squares_of_sorted_array(inp: List[int], expected: List[int]):
    assert squares_of_sorted_array(inp) == expected
