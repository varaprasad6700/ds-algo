"""
https://leetcode.com/problems/middle-of-the-linked-list/
"""
from typing import Optional

from src.helper.ListNode import ListNode


def middle_of_ll(head: Optional[ListNode]) -> Optional[ListNode]:
    n = 0
    temp = head
    while temp is not None:
        temp = temp.next
        n += 1
    i = 0
    while i < n // 2:
        head = head.next
        i += 1
    return head


def middle_of_ll_tortoise_hare(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


if __name__ == '__main__':
    print(middle_of_ll(ListNode.list_node_from_list([1, 2, 3, 4, 5])))
    print(middle_of_ll_tortoise_hare(ListNode.list_node_from_list([1, 2, 3, 4, 5])))
