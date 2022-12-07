"""
https://leetcode.com/problems/range-sum-of-bst/
"""
from typing import Optional

from src.helper.TreeNode import TreeNode


def range_sum_bst(root: Optional[TreeNode], low: int, high: int) -> int:
    if root is None:
        return 0
    else:
        if root.val < low:
            return range_sum_bst(root.right, low, high)
        elif root.val > high:
            return range_sum_bst(root.left, low, high)
        else:
            return root.val + range_sum_bst(root.left, low, high) + range_sum_bst(root.right, low, high)


if __name__ == '__main__':
    print(range_sum_bst(TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(7)), TreeNode(15, None, TreeNode(18))), 7, 15))
