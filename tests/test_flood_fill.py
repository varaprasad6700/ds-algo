import pytest

from src.ds.flood_fill import flood_fill


@pytest.mark.parametrize("image, sr, sc, color, expected", [
    ([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2, [[2, 2, 2], [2, 2, 0], [2, 0, 1]]),
    ([[0, 0, 0], [0, 0, 0]], 0, 0, 0, [[0, 0, 0], [0, 0, 0]])
])
def test_flood_fill(image, sr, sc, color, expected):
    assert flood_fill(image, sr, sc, color) == expected
