import pytest

from src.ds.count_and_say import count_and_say


@pytest.mark.parametrize("inp, expected", [
    (1, "1"),
    (2, "11"),
    (3, "21"),
    (4, "1211")
])
def test_count_and_say(inp: int, expected: str):
    assert count_and_say(inp) == expected
