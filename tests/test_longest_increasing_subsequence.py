import pytest

from src.ds.longest_increasing_subsequence import longest_increasing_subsequence


@pytest.mark.parametrize("inp, expected", [
    ([10, 9, 2, 5, 3, 7, 101, 18], 4),
    ([0, 1, 0, 3, 2, 3], 4),
    ([7, 7, 7, 7, 7, 7, 7], 1)
])
def test_longest_increasing_subsequence(inp, expected):
    assert longest_increasing_subsequence(inp) == expected
