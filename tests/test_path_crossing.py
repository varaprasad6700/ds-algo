import pytest
from typing import List

from src.ds.path_crossing import is_path_crossing


@pytest.mark.parametrize("path, expected", [
    ("NES", False),
    ("NESWW", True),
])
def test_is_path_crossing(path: str, expected: bool):
    assert is_path_crossing(path) == expected
