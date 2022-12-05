import pytest

from src.ds.sort_characters_by_frequency import frequency_sort


@pytest.mark.parametrize("inp, expected", [
    ("tree", "eetr")
])
def test_frequency_sort(inp: str, expected: str):
    assert frequency_sort(inp) == expected
