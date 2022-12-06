"""
https://leetcode.com/problems/odd-even-linked-list/description/
"""
from typing import Optional

from src.helper.ListNode import ListNode


def odd_even_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None
    else:
        curr = head
        odd_head = curr
        odd = odd_head
        curr = curr.next
        even_head = curr
        even = even_head
        flag = True
        while curr is not None:
            curr = curr.next
            if flag and curr is not None:
                odd.next = curr
                odd = odd.next
            else:
                even.next = curr
                even = even.next
            flag = not flag
        odd.next = even_head
        return odd_head


if __name__ == '__main__':
    print(odd_even_list(ListNode.list_node_from_list([1, 2, 3, 4, 5])))
