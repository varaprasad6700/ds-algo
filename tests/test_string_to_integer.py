import pytest

from src.ds.string_to_integer import string_to_integer


@pytest.mark.parametrize("s, out", [
    ("         -41", -41)
])
def test_string_to_integer(s, out):
    assert string_to_integer(s) == out
