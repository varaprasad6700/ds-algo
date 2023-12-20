from typing import List

import pytest

from src.ds.odd_even_linked_list import odd_even_list
from src.helper.ListNode import ListNode


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 3, 4, 5], [1, 3, 5, 2, 4]),
    ([2, 1, 3, 5, 6, 4, 7], [2, 3, 6, 7, 1, 5, 4])
])
def test_odd_even_list(inp: List[int], expected: List[int]):
    linked_list = odd_even_list(ListNode.list_node_from_list(inp))
    assert ListNode.get_list(linked_list) == expected
