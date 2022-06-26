import pytest
from src.ds.triplets_in_ap_from_sorted_array import triplets_in_ap_from_sorted_array

from src.ds.truncatable_primes_sum import truncatable_prime_sum


@pytest.mark.parametrize("numbers, expected", [
    ([5, 8, 9, 11, 12, 15], [[5, 8, 11], [9, 12, 15]])
])
def test_triplets_in_ap(numbers, expected):
    assert triplets_in_ap_from_sorted_array(numbers) == expected
