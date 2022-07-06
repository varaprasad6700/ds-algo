"""
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
from typing import Optional

from src.helper.TreeNode import TreeNode


def max_depth(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == '__main__':
    print(max_depth(TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))))
