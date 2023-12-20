import pytest

from src.ds.reverse_linkedlist import reverse_linked_list
from src.helper.ListNode import ListNode


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ([1, 2], [2, 1]),
    ([], [])
])
def test_reverse_linked_list(inp, expected):
    assert ListNode.get_list(reverse_linked_list(ListNode.list_node_from_list(inp))) == expected
