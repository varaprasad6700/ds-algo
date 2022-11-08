import pytest

from src.ds.ransom_note import can_construct


@pytest.mark.parametrize("rn, mag, expected", [
    ("a", "b", False),
    ("aa", "ab", False),
    ("aa", "aab", True),
])
def test_can_construct(rn, mag, expected):
    assert can_construct(rn, mag) == expected
