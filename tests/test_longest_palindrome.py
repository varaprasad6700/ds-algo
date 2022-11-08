import pytest

from src.ds.longest_palindrome import longest_palindrome


@pytest.mark.parametrize("inp, expected", [
    ("abccccdd", 7),
    ("a", 1)
])
def test_longest_palindrome(inp, expected):
    assert longest_palindrome(inp) == expected
