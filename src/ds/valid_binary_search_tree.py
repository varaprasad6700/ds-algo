"""
https://leetcode.com/problems/validate-binary-search-tree/
"""
from typing import Optional, List

from src.helper.TreeNode import TreeNode


def is_valid_bst(root: Optional[TreeNode]) -> bool:
    def in_order(root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        else:
            return in_order(root.left) + [root.val] + in_order(root.right)

    order = in_order(root)
    i = 1
    while i < len(order):
        if order[i] <= order[i - 1]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
    print(is_valid_bst(root))
