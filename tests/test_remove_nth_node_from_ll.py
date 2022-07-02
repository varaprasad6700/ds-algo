import pytest

from src.ds.remove_nth_node_from_ll import remove_nth_from_end
from src.helper.ListNode import ListNode


@pytest.mark.parametrize("inp, n, expected", [
    ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
    ([1], 1, []),
    ([1, 2], 1, [1])
])
def test_remove_nth_from_end(inp, n, expected):
    assert ListNode.get_list(remove_nth_from_end(ListNode.list_node_from_list(inp), n)) == expected
