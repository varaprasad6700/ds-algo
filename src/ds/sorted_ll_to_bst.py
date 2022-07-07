"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""
from typing import Optional

from src.helper.ListNode import ListNode
from src.helper.TreeNode import TreeNode


def sorted_linked_list_to_bst(head: Optional[ListNode]) -> Optional[TreeNode]:
    if head is None:
        return None

    def mid(head):
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        return slow, prev

    m, mb = mid(head)
    l = head
    r = m.next
    if mb is not None:
        mb.next = None
    elif mb is None:
        return TreeNode(m.val)
    return TreeNode(m.val, sorted_linked_list_to_bst(l), sorted_linked_list_to_bst(r))


if __name__ == '__main__':
    print(TreeNode.pre_order(sorted_linked_list_to_bst(ListNode.list_node_from_list([-10, -3, 0, 5, 9]))))
