import pytest

from src.ds.is_subsequence import is_subsequence


@pytest.mark.parametrize("s, t, expected", [
    ("abc", "ahbgdc", True),
    ("axc", "ahbgdc", False)
])
def test_is_subsequence(s, t, expected):
    assert is_subsequence(s, t) == expected
