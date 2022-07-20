import pytest

from src.ds.delete_and_earn import delete_and_earn


@pytest.mark.parametrize("inp, expected", [
    ([2, 2, 3, 3, 3, 4], 9),
    ([3, 4, 2], 6)
])
def test_delete_and_earn(inp, expected):
    assert delete_and_earn(inp) == expected
