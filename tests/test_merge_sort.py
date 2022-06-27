from typing import List

import pytest

from src.ds.merge_sort import merge_sort


@pytest.mark.parametrize("inp, expected", [
    ([], []),
    ([0, -1, 10, 5, 7, -6], [-6, -1, 0, 5, 7, 10]),
    ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
])
def test_merge_sort(inp: List, expected: List):
    merge_sort(inp, 0, len(inp) - 1)
    assert inp == expected
