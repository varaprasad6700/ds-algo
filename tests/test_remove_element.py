from typing import List

import pytest

from src.ds.remove_element import remove_element


@pytest.mark.parametrize("inp, val, expected", [
    ([3, 2, 2, 3], 3, [2, 2]),
    ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3])
])
def test_remove_element(inp: List[int], val: int, expected: List[int]):
    k = remove_element(inp, val)
    assert k == len(expected)
    assert sorted(inp[:k]) == sorted(expected)
