import pytest

from src.ds.remove_adjacent_letters import remove_duplicates


@pytest.mark.parametrize("inp, expected", [
    ("abbaca", "ca"),
    ("azxxzy", "ay")
])
def test_remove_duplicates(inp, expected):
    assert remove_duplicates(inp) == expected
