from typing import List

import pytest

from src.ds.container_with_most_water import max_area


@pytest.mark.parametrize("inp, expected", [
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1)
])
def test_max_area(inp: List[int], expected: int):
    assert max_area(inp) == expected
