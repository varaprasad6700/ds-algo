import pytest

from src.ds.pascal_triangle import pascal_triangle


@pytest.mark.parametrize("n, expected", [
    (5, [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]),
    (1, [[1]]),
    (3, [[1], [1, 1], [1, 2, 1]])
])
def test_pascal_triangle(n, expected):
    assert pascal_triangle(n) == expected
