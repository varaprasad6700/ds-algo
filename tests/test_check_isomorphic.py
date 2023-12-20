import pytest

from src.ds.check_isomorphic import check_isomorphic_onlyalpha, check_isomorphic


@pytest.mark.parametrize("s, t, expected", [
    ("egg", "add", True),
    ("foo", "bar", False),
    ("paper", "title", True),
    ("egs", "add", False)
])
def test_check_isomorphic(s, t, expected):
    assert check_isomorphic_onlyalpha(s, t) == expected
    assert check_isomorphic(s, t) == expected
