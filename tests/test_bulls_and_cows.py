import pytest

from src.ds.bulls_and_cows import bulls_and_cows


@pytest.mark.parametrize("secret, guess, expected", [
    ("1807", "7810", "1A3B"),
    ("1123", "0111", "1A1B")
])
def test_bulls_and_cows(secret, guess, expected):
    assert bulls_and_cows(secret, guess) == expected
