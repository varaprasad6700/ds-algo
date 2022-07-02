import pytest

from src.ds.middle_of_linked_list import middle_of_ll, middle_of_ll_tortoise_hare
from src.helper.ListNode import ListNode


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 3, 4, 5], [3, 4, 5]),
    ([1, 2, 3, 4, 5, 6], [4, 5, 6])
])
def test_middle_of_ll(inp, expected):
    temp = ListNode.list_node_from_list(inp)
    assert ListNode.get_list(middle_of_ll(temp)) == expected
    temp = ListNode.list_node_from_list(inp)
    assert ListNode.get_list(middle_of_ll_tortoise_hare(temp)) == expected
