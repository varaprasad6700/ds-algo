import pytest

from src.ds.number_of_laser_beams import number_of_beams


@pytest.mark.parametrize("bank, expected", [
    (["011001", "000000", "010100", "001000"], 8),
    (["000", "111", "000"], 0)
])
def test_number_of_beams(bank, expected):
    assert number_of_beams(bank) == expected
