import pytest

from src.ds.first_unique_character_in_string import first_unique_char


@pytest.mark.parametrize("inp, expected", [
    ("leetcode", 0),
    ("loveleetcode", 2),
    ("aabb", -1)
])
def test_first_unique_char(inp, expected):
    assert first_unique_char(inp) == expected
