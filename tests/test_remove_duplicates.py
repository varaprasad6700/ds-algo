from typing import List

import pytest

from src.ds.remove_duplicates import remove_duplicates


@pytest.mark.parametrize("inp, expected", [
    ([1, 1, 2], [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4])
])
def test_remove_duplicates(inp: List[int], expected: List[int]):
    k = remove_duplicates(inp)
    assert k == len(expected)
    for i in range(k):
        assert inp[i] == expected[i]
