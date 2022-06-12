import pytest

from src.ds.double_base_palindrome_sum import double_base_palindrome_sum




@pytest.mark.parametrize("number, expected", [
    (1000000, 872187)
])
def test_double_base_palin_sum(number, expected):
    assert double_base_palindrome_sum(number) == expected
