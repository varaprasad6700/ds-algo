from typing import List

import pytest

from src.ds.search_insertion_position import search_insertion_position


@pytest.mark.parametrize("inp, target, expected", [
    ([1, 3, 5, 6], 5, 2),
    ([1, 3, 5, 6], 2, 1),
    ([1, 3, 5, 6], 7, 4),
])
def test_search_insertion_position(inp: List[int], target: int, expected: int):
    assert search_insertion_position(inp, target) == expected
