import pytest

from src.ds.linked_list_is_palindrome import is_palindrome
from src.helper.ListNode import ListNode


@pytest.mark.parametrize("inp, expected", [
    ([1, 2, 2, 1], True),
    ([1], True),
    ([1, 2], False)
])
def test_is_palindrome(inp, expected):
    assert is_palindrome(ListNode.list_node_from_list(inp)) == expected
