from typing import List

import pytest

from src.ds.unique_number_of_occurence import unique_occurrence


@pytest.mark.parametrize("inp, out", [
    ([1, 2, 2, 1, 1, 3], True),
    ([1, 2], False),
    ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True)
])
def test_unique_occurrence(inp: List[int], out: bool):
    assert unique_occurrence(inp) == out
