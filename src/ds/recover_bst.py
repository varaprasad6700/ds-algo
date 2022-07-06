"""

"""
from typing import Optional

from src.helper.TreeNode import TreeNode


def recover_tree(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    first: Optional[TreeNode] = None
    second: Optional[TreeNode] = None
    prev: Optional[TreeNode] = None

    def in_order(root):
        nonlocal first
        nonlocal second
        nonlocal prev
        if root is None:
            return
        in_order(root.left)
        if first is None and prev is not None and prev.val >= root.val:
            first = prev
        if first is not None and prev.val >= root.val:
            second = root
        prev = root
        in_order(root.right)

    in_order(root)
    first.val, second.val = second.val, first.val


if __name__ == '__main__':
    tree = TreeNode(1, TreeNode(3, None, TreeNode(2)))
    recover_tree(tree)
