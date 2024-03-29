import pytest

from src.ds.number_of_islands import number_of_islands


@pytest.mark.parametrize("grid, expected", [
    ([
         ["1", "1", "1", "1", "0"],
         ["1", "1", "0", "1", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "0", "0", "0"]
     ], 1),
    ([
         ["1", "1", "0", "0", "0"],
         ["1", "1", "0", "0", "0"],
         ["0", "0", "1", "0", "0"],
         ["0", "0", "0", "1", "1"]
     ], 3)
])
def test_number_of_islands(grid, expected):
    assert number_of_islands(grid) == expected
