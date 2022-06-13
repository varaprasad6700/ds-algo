import pytest

from src.ds.prime_number import is_prime


@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (5, True),
    (7, True),
    (11, True),
    (71, True),
    (3907, True),
    (4, False),
    (1512, False)
])
def test_is_prime(number: int, expected: bool):
    assert is_prime(number) is expected
