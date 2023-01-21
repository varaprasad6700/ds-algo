from typing import List

import pytest

from src.ds.non_decreasing_subsequence import find_subsequences


@pytest.mark.parametrize("inp, expected", [
    ([4, 6, 7, 7], [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]),
    ([4, 4, 3, 2, 1], [[4, 4]])
])
def test_find_subsequences(inp: List[int], expected: List[List[int]]):
    actual: List[List[int]] = find_subsequences(inp)
    actual_copy = actual.copy()
    for i in actual:
        if i in expected:
            expected.remove(i)
            actual_copy.remove(i)
    assert len(expected) == 0
    assert len(actual_copy) == 0
