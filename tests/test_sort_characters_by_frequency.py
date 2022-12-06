from typing import List

import pytest

from src.ds.sort_characters_by_frequency import frequency_sort


@pytest.mark.parametrize("inp, expected", [
    ("tree", ["eetr", "eert"]),
    ("cccaaa", ["aaaccc", "cccaaa"]),
    ("Aabb", ["bbAa", "bbaA"])
])
def test_frequency_sort(inp: str, expected: List[str]):
    assert frequency_sort(inp) in expected
