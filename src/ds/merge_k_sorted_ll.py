"""
https://leetcode.com/problems/merge-k-sorted-lists/
"""
from typing import List, Optional

from src.helper.ListNode import ListNode


def merge_k_sorted_lists_1by1(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    head = ListNode()
    curr = head
    while True:
        min_val = 10 ** 5
        min_ind = -1
        for i in range(len(lists)):
            if lists[i] is not None and min_val > lists[i].val:
                min_val = lists[i].val
                min_ind = i
        if min_ind == -1:
            break
        else:
            curr.next = ListNode(min_val)
            curr = curr.next
            lists[min_ind] = lists[min_ind].next
    return head.next


def merge_k_sorted_list_according_to_len(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    lens = [0 for _ in lists]
    for i in range(len(lists)):
        temp = lists[i]
        while temp is not None:
            temp = temp.next
            lens[i] += 1
    print(lens)


if __name__ == '__main__':
    inp = [ListNode.list_node_from_list(i) for i in ([1, 4, 5], [1, 3, 4], [2, 6])]
    out = merge_k_sorted_lists_1by1(inp)
    inp = [ListNode.list_node_from_list(i) for i in ([1, 4, 5], [1, 3, 4], [2, 6])]
    out_ = merge_k_sorted_list_according_to_len(inp)
    print(out, out_)
