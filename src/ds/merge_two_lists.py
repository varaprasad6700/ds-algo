"""
https://leetcode.com/problems/merge-two-sorted-lists/
"""


from typing import Optional
from src.helper.ListNode import ListNode


def merge_two_lists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    head = ListNode(0)
    curr = head
    while list1 is not None and list2 is not None:
        if list1.val <= list2.val:
            temp = ListNode(list1.val)
            curr.next = temp
            curr = temp
            list1 = list1.next
        else:
            temp = ListNode(list2.val)
            curr.next = temp
            curr = temp
            list2 = list2.next
    while list1 is not None:
        temp = ListNode(list1.val)
        curr.next = temp
        curr = temp
        list1 = list1.next
    while list2 is not None:
        temp = ListNode(list2.val)
        curr.next = temp
        curr = temp
        list2 = list2.next
    return head.next


if __name__ == '__main__':
    print(merge_two_lists(ListNode.list_node_from_list(
        [1, 2, 4]), ListNode.list_node_from_list([1, 3, 4])))
