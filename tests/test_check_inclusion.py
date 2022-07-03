import pytest

from src.ds.check_inclusion import check_inclusion


@pytest.mark.parametrize("s1, s2, expected", [
    ("ab", "eidbaooo", True),
    ("ab", "a", False),
    ("ab", "eidboaoo", False)
])
def test_check_inclusion(s1, s2, expected):
    assert check_inclusion(s1, s2) == expected
