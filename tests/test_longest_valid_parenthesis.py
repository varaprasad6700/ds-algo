import pytest

from src.ds.longest_valid_parenthesis import longest_valid_parenthesis


@pytest.mark.parametrize("inp, expected", [
    (")()())", 4),
    ("(()", 2),
    ("", 0)
])
def test_longest_valid_parenthesis(inp, expected):
    assert longest_valid_parenthesis(inp) == expected
