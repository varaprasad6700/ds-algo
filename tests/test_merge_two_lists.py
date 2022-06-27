from typing import List

import pytest

from src.ds.merge_two_lists import merge_two_lists
from src.helper.ListNode import ListNode


@pytest.mark.parametrize("l1, l2, expected", [
    ([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
    ([], [], []),
    ([], [0], [0])
])
def test_merge_two_lists(l1: List[int], l2: List[int], expected: List[int]):
    ll1 = ListNode.list_node_from_list(l1)
    ll2 = ListNode.list_node_from_list(l2)
    actual = ListNode.get_list(merge_two_lists(ll1, ll2))
    assert actual == expected
