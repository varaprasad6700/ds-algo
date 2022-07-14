from typing import List

import pytest

from src.ds.trapping_rain_water import trap_rain_water


@pytest.mark.parametrize("inp, expected", [
    ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6)
])
def test_trap_rain_water(inp: List[int], expected: int):
    assert trap_rain_water(inp) == expected
