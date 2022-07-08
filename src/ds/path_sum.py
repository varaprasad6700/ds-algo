"""
https://leetcode.com/problems/path-sum/
"""
from typing import Optional

from src.helper.TreeNode import TreeNode


def has_path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
    if root is None:
        return False
    elif root.left is None and root.right is None:
        return target_sum == root.val
    else:
        rem = target_sum - root.val
        return has_path_sum(root.left, rem) or has_path_sum(root.right, rem)


if __name__ == '__main__':
    print(has_path_sum(TreeNode(1, TreeNode(2), TreeNode(3)), 5))
