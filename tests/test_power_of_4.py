import pytest

from src.ds.power_of_4 import is_power_of_four


@pytest.mark.parametrize("inp, expected", [
    (1024, True),
    (512, False),
    (1025, False),
    (0, False)
])
def test_is_power_of_four(inp, expected):
    assert is_power_of_four(inp) == expected
