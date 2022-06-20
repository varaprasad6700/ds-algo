from typing import List

import pytest

from src.ds.quick_sort import quick_sort


@pytest.mark.parametrize("inp, expected", [
    ([], []),
    ([0, -1, 10, 5, 7, -6], [-6, -1, 0, 5, 7, 10]),
    ([0, 1, 2, 3, 4], [0, 1, 2, 3, 4])
])
def test_quicksort(inp: List, expected: List):
    quick_sort(inp, 0, len(inp) - 1)
    assert inp == expected
