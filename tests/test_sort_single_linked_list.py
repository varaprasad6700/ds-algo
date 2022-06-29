import pytest

from src.ds.sort_single_linked_list import sort_single_ll
from src.helper.ListNode import ListNode


@pytest.mark.parametrize("inp, expected", [
    ([], []),
    ([23, 44, 1, 3, 2, 50, 7, 100], [1, 2, 3, 7, 23, 44, 50, 100]),
    ([10, 9, 8, 7, 6, 5, 4], [4, 5, 6, 7, 8, 9, 10]),
    ([-1], [-1])
])
def test_sort_single_ll(inp, expected):
    assert ListNode.get_list(sort_single_ll(ListNode.list_node_from_list(inp))) == expected
