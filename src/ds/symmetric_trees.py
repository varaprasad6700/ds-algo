"""
https://leetcode.com/problems/symmetric-tree/
"""
from typing import Optional

from src.helper.TreeNode import TreeNode


def is_symmetric(root: Optional[TreeNode]) -> bool:
    def symmetry_check(l: Optional[TreeNode], r: Optional[TreeNode]) -> bool:
        if l is None or r is None:
            return l is None and r is None
        elif l.val != r.val:
            return False
        else:
            return symmetry_check(l.left, r.right) and symmetry_check(l.right, r.left)
    if root is None:
        return True
    else:
        return symmetry_check(root.left, root.right)


if __name__ == '__main__':
    print(is_symmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))))
