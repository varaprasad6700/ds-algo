from typing import List

import pytest

from src.ds.widest_vertical_area import max_width_of_vertical_area


@pytest.mark.parametrize("inp, expected", [
    ([[8, 7],[9,9],[7,4],[9,7]], 1),
    ([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]], 3)
])
def test_max_width_of_vertical_area(inp: List[List[int]], expected: int):
    assert max_width_of_vertical_area(inp) == expected
