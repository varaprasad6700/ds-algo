import pytest

from src.ds.close_strings import close_strings


@pytest.mark.parametrize("w1, w2, expected", [
    ("abc", "bca", True),
    ("a", "aa", False),
    ("cabbba", "abbccc", True),
])
def test_close_strings(w1: str, w2: str, expected: bool):
    assert close_strings(w1, w2) == expected
