"""
https://leetcode.com/problems/same-tree/
"""
from typing import Optional

from src.helper.TreeNode import TreeNode


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if p is None or q is None:
        return p is None and q is None
    elif p.val == q.val:
        return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False


if __name__ == '__main__':
    print(is_same_tree(TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3))))
    print(is_same_tree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2))))
