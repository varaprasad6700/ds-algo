import pytest

from src.ds.roman_to_int import roman_to_int


@pytest.mark.parametrize("roman, expected", [
    ("MCMXCIV", 1994),
    ("III", 3),
    ("LVIII", 58),
])
def test_roman_to_int(roman, expected):
    assert roman_to_int(roman) == expected
