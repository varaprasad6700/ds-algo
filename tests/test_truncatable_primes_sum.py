import pytest

from src.ds.truncatable_primes_sum import truncatable_prime_sum


@pytest.mark.parametrize("number, expected", [
    (11, 748317)
])
def test_truncatable_prime_sum(number, expected):
    assert truncatable_prime_sum(number) == expected
