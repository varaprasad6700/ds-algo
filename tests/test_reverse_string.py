import pytest

from src.ds.reverse_string import reverse_string


@pytest.mark.parametrize("inp, expected", [
    (["h", "e", "l", "l", "o"], ["o", "l", "l", "e", "h"]),
    (["H", "a", "n", "n", "a", "h"], ["h", "a", "n", "n", "a", "H"])
])
def test_reverse_string(inp, expected):
    reverse_string(inp)
    assert inp == expected
