from typing import List

import pytest

from src.ds.pythagorean_triplet import pythagorean_triplet


@pytest.mark.parametrize("limit, expected", [
    (1000, [200, 375, 425])
])
def test_pythagorean_triplet(limit: int, expected: List[int]):
    assert pythagorean_triplet(limit) == expected
