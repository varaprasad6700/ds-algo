import pytest

from src.ds.string_halves_are_alike import halves_are_alike


@pytest.mark.parametrize("inp, expected", [
    ("book", True),
    ("textbook", False)
])
def test_halves_are_alike(inp: str, expected: bool):
    assert halves_are_alike(inp) == expected
