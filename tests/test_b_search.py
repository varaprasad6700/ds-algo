from typing import List

import pytest

from src.ds.binary_search import search


@pytest.mark.parametrize("arr, target, expected", [
    ([-1, 0, 3, 5, 9, 12], 9, 4),
    ([-1, 0, 3, 5, 9, 12], 2, -1)
])
def test_b_search(arr, target: int, expected: int):
    assert search(arr, target) == expected
