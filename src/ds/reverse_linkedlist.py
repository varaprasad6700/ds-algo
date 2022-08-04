"""
https://leetcode.com/problems/reverse-linked-list/
"""
from typing import Optional

from src.helper.ListNode import ListNode


def reverse_linked_list(head: Optional[ListNode]) -> Optional[ListNode]:
    prev = None
    curr = head
    while curr is not None:
        curr.next, prev, curr = prev, curr, curr.next
    return prev


if __name__ == '__main__':
    print(reverse_linked_list(ListNode.list_node_from_list([1, 2, 3, 4, 5])))
