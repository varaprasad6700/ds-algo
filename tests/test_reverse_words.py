import pytest

from src.ds.reverse_words import reverse_words


@pytest.mark.parametrize("inp, expected", [
    ("Let's take LeetCode contest","s'teL ekat edoCteeL tsetnoc"),
    ("God Ding", "doG gniD")
])
def test_reverse_words(inp, expected):
    assert reverse_words(inp) == expected
