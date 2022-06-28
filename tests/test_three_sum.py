from typing import List

import pytest

from src.ds.three_sum import three_sum


@pytest.mark.parametrize("inp, expected", [
    ([[-1, 0, 1, 2, -1, -4], [[-1, 0, 1], [-1, -1, 2]]])
])
def test_three_sum(inp: List[int], expected: List[List[int]]):
    actual = three_sum(inp)
    assert not set([tuple(i) for i in actual]) ^ set([tuple(i) for i in expected])
