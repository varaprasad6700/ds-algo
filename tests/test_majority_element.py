from typing import List

import pytest

from src.ds.majority_element import majority_element_dict, majority_element_div_and_conquer


@pytest.mark.parametrize("numbers, expected", [
    ([2, 2, 1, 1, 1, 2, 2], 2),
    ([3, 2, 3], 3)
])
def test_double_base_palin_sum(numbers: List[int], expected: int):
    assert majority_element_dict(numbers) == expected
    assert majority_element_div_and_conquer(numbers, 0, len(numbers) - 1) == expected
