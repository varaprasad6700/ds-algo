"""

"""
from typing import Optional

from src.helper.ListNode import ListNode


def is_palindrome(head: Optional[ListNode]) -> bool:
    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    prev = None
    mid = slow
    while mid is not None:
        temp = mid.next
        mid.next = prev
        prev = mid
        mid = temp
    mid = prev
    while head is not None and mid is not None:
        if head.val != mid.val:
            return False
        head = head.next
        mid = mid.next
    return True


if __name__ == '__main__':
    print(is_palindrome(ListNode.list_node_from_list([1, 2, 2, 1])))
