import pytest

from src.ds.running_sum import running_sum


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 3, 4], [1, 3, 6, 10]),
    ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
    ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17])
])
def test_running_sum(inp, expected):
    assert running_sum(inp) == expected
