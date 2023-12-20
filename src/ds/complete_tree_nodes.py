"""
https://leetcode.com/problems/count-complete-tree-nodes/description/
"""
from typing import Optional

from src.helper.TreeNode import TreeNode


def count_nodes(root: Optional[TreeNode]) -> int:
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    else:
        return 1 + count_nodes(root.left) + count_nodes(root.right)


if __name__ == '__main__':
    print(count_nodes(TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6)))))
