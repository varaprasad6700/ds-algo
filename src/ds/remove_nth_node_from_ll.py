"""
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
from typing import Optional

from src.helper.ListNode import ListNode


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    slow = fast = head
    for i in range(n):
        fast = fast.next
    if fast is None:
        return slow.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
    return head


if __name__ == '__main__':
    print(remove_nth_from_end(ListNode.list_node_from_list([1, 2, 3, 4, 5]), 2))
