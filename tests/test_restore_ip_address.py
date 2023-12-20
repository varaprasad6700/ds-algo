from typing import List

import pytest

from src.ds.restore_ip_address import restore_ip_addresses


@pytest.mark.parametrize("inp, expected", [
    ("25525511135", ["255.255.11.135", "255.255.111.35"]),
    ("0000", ["0.0.0.0"]),
    ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])
])
def test_restore_ip_addresses(inp: str, expected: List[str]):
    actual = restore_ip_addresses(inp)
    actual_copy = actual.copy()
    for i in actual:
        if i in expected:
            expected.remove(i)
            actual_copy.remove(i)
    assert len(expected) == 0
    assert len(actual_copy) == 0
