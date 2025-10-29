import pytest

from src.ds.smallest_number_with_all_set_bits import smallest_number


@pytest.mark.parametrize("inp, out", [
    (5, 7),
    (10, 15),
    (3, 3),
])
def test_smallest_number(inp: int, out: int):
    assert smallest_number(inp) == out