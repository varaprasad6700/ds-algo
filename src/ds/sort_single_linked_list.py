"""
Given a singly linked list of N elements,
how could you sort it in guaranteed O(N log N) time, stably,
and with O(1) extra space?
"""
from typing import Optional

from src.helper.ListNode import ListNode


def find_mid(head: ListNode) -> ListNode:
    n = 0
    temp = head
    while temp is not None:
        n += 1
        temp = temp.next
    temp = head
    i = 0
    while i < (n // 2) - 1:
        i += 1
        temp = temp.next
    return temp


def merge(left: ListNode, right: ListNode):
    head = ListNode()
    temp = head
    while left is not None and right is not None:
        if left.val <= right.val:
            temp.next = left
            temp = temp.next
            left = left.next
        else:
            temp.next = right
            temp = temp.next
            right = right.next
    if left is not None:
        temp.next = left
    if right is not None:
        temp.next = right
    return head.next


def sort_single_ll(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None or head.next is None:
        return head
    else:
        mid = find_mid(head)
        left = head
        right = mid.next
        mid.next = None
        left = sort_single_ll(left)
        right = sort_single_ll(right)
        return merge(left, right)


if __name__ == '__main__':
    print(sort_single_ll(ListNode.list_node_from_list([23, 44, 1, 3, 2, 50, 7, 100])))
